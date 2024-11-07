from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
# views.py
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from Aplicaciones.user.models import Profile

# Funciones auxiliares para verificar permisos
def is_admin(user):
    return user.groups.filter(name='Administrador').exists()

def is_staff(user):
    return user.groups.filter(name='Personal').exists()
# Create your views here.
@login_required
@user_passes_test(is_admin, login_url='error')
def lUsuarios(request):
    # Obtenemos la lista de todos los usuarios registrados
  
    users = User.objects.filter(profile__is_internal=False)
    return render(request, 'listaUsuarios.html', {"object_list": users})

@login_required
@user_passes_test(is_admin, login_url='error')
def lInternos(request):
    # Obtenemos la lista de todos los usuarios registrados
  
    users = User.objects.filter(profile__is_internal=True)
    return render(request, 'listaInternos.html', {"object_list": users})



@login_required
@user_passes_test(is_admin, login_url='error')

def desactivar_usuario(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        user.delete()  # Esto eliminará al usuario permanentemente de la base de datos
        messages.success(request, f'Usuario {user.username} eliminado permanentemente.')
        return redirect('lInternos')  # Reemplaza con el nombre de tu URL

    # Si deseas, puedes agregar una confirmación antes de eliminar
    return render(request, 'confirmar_eliminacion.html', {'user': user})

@login_required
@user_passes_test(is_admin, login_url='error')

def desactivar_usuario_publico(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        user.delete()  # Esto eliminará al usuario permanentemente de la base de datos
        messages.success(request, f'Usuario {user.username} eliminado permanentemente.')
        return redirect('lInternos')  # Reemplaza con el nombre de tu URL

    # Si deseas, puedes agregar una confirmación antes de eliminar
    return render(request, 'confirmar_eliminacion.html', {'user': user})

