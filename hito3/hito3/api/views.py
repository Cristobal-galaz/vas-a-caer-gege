from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import csv
import logging
from selenium.common.exceptions import NoSuchElementException
from rest_framework import viewsets
from .models import ExAlumno
from .serializers import ExAlumnoSerializer


# Configuración del logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class ExAlumnoViewSet(viewsets.ModelViewSet):
    queryset = ExAlumno.objects.all()
    serializer_class = ExAlumnoSerializer

def init_driver(browser='chrome'):
    logger.info(f"Inicializando el driver para {browser}")
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    elif browser == 'edge':
        options = webdriver.EdgeOptions()
        options.add_argument("--headless")
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)
    else:
        raise ValueError("Navegador no soportado: elige 'chrome', 'firefox' o 'edge'.")
    return driver

def realizar_busqueda(nombre, profesion, ciudad, region, correo, browser='chrome'):
    driver = None
    try:
        consulta = f"{nombre} {profesion} {ciudad}, {region}, {correo}"
        logger.info(f"Realizando búsqueda para: {consulta}")
        
        driver = init_driver(browser)
        driver.get("https://www.google.com")
        
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(consulta)
        search_box.submit()

        logger.info(f"Esperando a que se carguen los resultados de búsqueda")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.g"))
        )

        logger.info(f"Extrayendo información de los resultados de búsqueda para la consulta: {consulta}")
        results = driver.find_elements(By.CSS_SELECTOR, "div.g")

        resultados = []
        for result in results:
            try:
                title = result.find_element(By.CSS_SELECTOR, "h3").text
                link = result.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                try:
                    snippet = result.find_element(By.CSS_SELECTOR, "span.st").text  # Ajuste para obtener snippet
                except NoSuchElementException:
                    snippet = "No se encontró el snippet"

                resultados.append({'title': title, 'link': link, 'snippet': snippet})
            except Exception as e:
                logger.error(f"Error al extraer información de un resultado: {e}")

        return resultados
    except Exception as e:
        logger.error(f"Error durante la búsqueda: {e}")
        return []
    finally:
        if driver:
            driver.quit()

@api_view(['GET', 'POST'])
def search_exalumno(request):
    if request.method == 'POST' or (request.method == 'GET' and 'refresh' in request.GET):
        csv_file = request.FILES.get('csv_file') if request.method == 'POST' else None
        browser = request.POST.get('browser', request.session.get('browser', 'chrome'))

        resultados = []

        if csv_file:
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            for row in reader:
                nombres = row.get('nombres')
                profesion = row.get('profesion')
                ciudad = row.get('ciudad')
                region = row.get('region', '')  # Obtener región desde el CSV si está presente
                correo = row.get('correo')

                if nombres:  # Solo realiza la búsqueda si el nombre está presente
                    resultado = realizar_busqueda(nombres, profesion, ciudad, region, correo, browser)
                    if resultado:
                        for res in resultado:
                            resultados.append([nombres, profesion, ciudad, region, correo, res['link']])

            # Guardar resultados en la sesión para permitir la descarga y refresco
            request.session['resultados'] = resultados
            request.session['browser'] = browser

            return render(request, 'search_exalumno.html', {'resultados': resultados})

        else:
            nombres = request.POST.get('nombres', request.session.get('nombres'))
            profesion = request.POST.get('profesion', request.session.get('profesion'))
            ciudad = request.POST.get('ciudad', request.session.get('ciudad'))
            region = request.POST.get('region', request.session.get('region', ''))
            correo = request.POST.get('correo', request.session.get('correo'))

            if not nombres and not profesion and not ciudad and not correo:
                return render(request, 'search_exalumno.html', {'error': 'Proporcione al menos un parámetro de búsqueda o suba un archivo CSV.'})

            resultado = realizar_busqueda(nombres, profesion, ciudad, region, correo, browser)

            if resultado:
                for res in resultado:
                    resultados.append({'title': res['title'], 'link': res['link'], 'snippet': res['snippet']})

            # Guardar resultados en la sesión para permitir la descarga y refresco
            request.session['resultados'] = resultados
            request.session['nombres'] = nombres
            request.session['profesion'] = profesion
            request.session['ciudad'] = ciudad
            request.session['region'] = region
            request.session['correo'] = correo
            request.session['browser'] = browser

        if not resultados:
            return render(request, 'search_exalumno.html', {'error': 'No se encontraron datos'})

        return render(request, 'search_exalumno.html', {'resultados': resultados})

    return render(request, 'search_exalumno.html')

def download_csv(request):
    resultados = request.session.get('resultados')

    if resultados:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="resultados_exalumnos.csv"'

        writer = csv.writer(response)
        writer.writerow(['Nombres', 'Profesión', 'Ciudad', 'Región', 'Correo', 'Enlace'])
        for resultado in resultados:
            writer.writerow(resultado)

        return response

    return render(request, 'search_exalumno.html', {'error': 'No hay resultados para descargar.'})

def inicio(request):
    return render(request, 'inicio.html')