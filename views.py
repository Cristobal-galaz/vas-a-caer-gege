# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import RegistrationForm
from .models import IA, Favorita
from django.core.paginator import Paginator






def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('user_login_success'))
        else:
            return render(request, 'pagina_principal.html', {'access_message': 'Credenciales inválidas'})
    return render(request, 'home.html')

def user_login_success(request):
    return render(request, 'successful.html')

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email, password=password)
            if user:
                return redirect('registration_success', username=username)
        else:
            return HttpResponse('Error en el formulario de registro')
    else:
        form = RegistrationForm()
    return render(request, 'registre.html', {'form': form})

def registration_success(request, username):
    return render(request, 'registre.html', {'username': username})

def casa(request):
    ias = IA.objects.all()
    return render(request, "pagina_principal.html", {"ias": ias})

def marcar_favorita(request, ia_id):
    if request.user.is_authenticated:
        ia = IA.objects.get(pk=ia_id)
        favorita, created = Favorita.objects.get_or_create(usuario=request.user, ia=ia)
        if created:
            mensaje = "IA marcada como favorita"
        else:
            favorita.delete()
            mensaje = "IA eliminada de las favoritas"
        return HttpResponse(mensaje)
    else:
        return HttpResponse('Inicia sesión para marcar como favorita')

def favoritas(request):
    if request.user.is_authenticated:
        favoritas = Favorita.objects.filter(usuario=request.user)
        return render(request, "favoritas.html", {"favoritas": favoritas})
    else:
        return HttpResponse('Inicia sesión para ver tus favoritas')
    
def pagina_principal(request):
    categoria_filtrada = request.GET.get('categoria', None)
    page_number = request.GET.get('page', 1)
    items_per_page = 20  # Número de IAs a mostrar por página

    if categoria_filtrada:
        ias = IA.objects.filter(categoria=categoria_filtrada)
    else:
        ias = IA.objects.all()
    
    paginator = Paginator(ias, items_per_page)
    page_obj = paginator.get_page(page_number)

    categorias_unicas = IA.objects.values_list('categoria', flat=True).distinct()
    
    return render(request, 'pagina_principal.html', {
        'page_obj': page_obj,
        'categorias': categorias_unicas,
        'categoria_filtrada': categoria_filtrada
    })
def obtener_datos(request):
    ias = IA.objects.all()
    return render(request, 'pagina_principal.html', {'ias': ias})

def logout_view(request):
    logout(request)
    return redirect('pagina_principal')

