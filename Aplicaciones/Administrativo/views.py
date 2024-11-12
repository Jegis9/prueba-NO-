from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required #importa libreria para hacer de la pagina requerido el login para poder verla
from django.contrib.auth.models import User
# importar libreria para el registro de usuarios
from django.contrib.auth.forms import UserCreationForm
from Aplicaciones.user.forms import CreateUserForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views import View





def errores(request, exception=None):
    return render(request, 'errores.html', status=404)

def error_500(request):
    return render(request, '500.html', status=500)









