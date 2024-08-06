# api/scraper/linkedin_scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_linkedin(name):
    search_url = f"https://www.linkedin.com/search/results/all/?keywords={name}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    results = []
    for profile in soup.find_all('div', class_='search-result__info'):
        name = profile.find('span', class_='name').get_text(strip=True)
        occupation = profile.find('span', class_='subline-level-1').get_text(strip=True)
        location = profile.find('span', class_='subline-level-2').get_text(strip=True)
        results.append({'name': name, 'occupation': occupation, 'location': location})
    
    return results

def scrape_linkedin_profile(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Aquí deberías definir cómo extraer los datos específicos del perfil
    profile_data = {
        'nombre': 'John Doe',
        'profesion': 'Software Engineer',
        'ciudad': 'San Francisco',
        'tipo_trabajo': 'Full-time',
        'sector': 'Tech',
        'contacto': 'johndoe@example.com'
    }

    return profile_data

