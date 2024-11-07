from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from.models import Vehiculos, Mantenimiento
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .forms import VEHForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.utils import timezone
from Aplicaciones.user.models import Profile

# Funciones auxiliares para verificar permisos
def is_admin(user):
    return user.groups.filter(name='Administrador').exists()

def is_staff(user):
    return user.groups.filter(name='Personal').exists()
def is_admin_or_staff(user):
    return user.is_authenticated and user.groups.filter(name__in=['Administrador', 'Personal']).exists()


@login_required
@user_passes_test(is_admin_or_staff, login_url='error')
def vehiculos(request):
    if request.method == 'POST':
        user = request.user  # Usuario en sesión
        placas = request.POST.get('placa')
        tipo_vehiculo = request.POST.get('tipo')

        Vehiculos.objects.create(user=user, placas=placas,  tipo_vehiculo=tipo_vehiculo)
        return redirect('vehiculos')
    
    vehiculos_list = Vehiculos.objects.all()  # Mostrar solo los vehículos del usuario en sesión
    return render(request, 'vehiculos.html', {'vehiculos_list': vehiculos_list})


@login_required
@user_passes_test(is_admin, login_url='error')
def eliminar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculos, id=vehiculo_id)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('vehiculos') 
    return render(request, 'vehiculos.html')




@login_required
@user_passes_test(is_admin_or_staff, login_url='error')
def mantenimientoVehiculos(request, vehiculo_id):
    vehiculo = Vehiculos.objects.get(id=vehiculo_id)  # Asegurarse que el vehículo pertenezca al usuario
    if request.method == 'POST':
        estado = request.POST.get('estado') == 'on'
        descripcion = request.POST.get('descripcion')

        Mantenimiento.objects.create(vehiculo=vehiculo, estado=estado, descripcion=descripcion)


        
        messages.success(request, "El vehículo ha sido reportado.")
        return redirect('vehiculos')
    

    return render(request, 'vehiculos.html')


@login_required
@user_passes_test(is_admin, login_url='error')
def lVehiculos(request):
    # Filtrar solo los vehículos que no han sido arreglados
    estados = Mantenimiento.objects.filter(estado=False)  
    return render(request, 'reportesVehiculos.html', {"estados": estados})



@login_required
@user_passes_test(is_admin, login_url='error')
def marcar_arreglado_vehiculo(request, vehiculo_id):
    estado = get_object_or_404(Mantenimiento, id=vehiculo_id)
    estado.estado = True  # Cambia el estado a "arreglado"
    estado.save()
    messages.success(request, "El vehículo ha sido marcado como arreglado.")
    return redirect('mantenimiento')  # Redirige a la lista de mantenimiento


@login_required
@user_passes_test(is_admin, login_url='error')
def editar_vehiculos(request, codigo_vehiculo):
    vehiculo = get_object_or_404(Vehiculos, id=codigo_vehiculo)
    if request.method == 'POST':
        form = VEHForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            messages.success(request, 'EPP editado correctamente.')
            return redirect('vehiculos')  # Asegúrate de que 'lista_epps' es el nombre correcto de tu vista
    else:
        form = VEHForm(instance=vehiculo)
    return render(request, 'editar_vehiculo.html', {'form': form})


# from django.contrib.auth.decorators import login_required, user_passes_test
# from django.core.mail import send_mail
# from django.db.models import Sum
# from django.shortcuts import render
# from django.conf import settings
# from .models import Servicio, Vehiculos

# @login_required
# @user_passes_test(is_admin_or_staff, login_url='error')
# def vista_kilometraje(request):
#     # Agrupar los servicios por unidad y calcular el kilometraje total por unidad
#     unidades_km = Servicio.objects.filter(activo=True).values('unidad__id', 'unidad__nombre').annotate(total_km=Sum('km_recorridos'))

#     # Lista para almacenar las unidades próximas a los 3500 km
#     unidades_proximas_a_mantenimiento = []

#     # Verificar si alguna unidad está cerca de los 3500 km
#     for unidad in unidades_km:
#         if unidad['total_km'] >= 3500:
#             unidades_proximas_a_mantenimiento.append(unidad)
    
#     # Enviar un correo si hay unidades próximas a mantenimiento
#     if unidades_proximas_a_mantenimiento:
#         subject = 'Notificación de Mantenimiento de Vehículos'
#         message = 'Las siguientes unidades están próximas a los 3500 km y requieren mantenimiento:\n\n'
#         for unidad in unidades_proximas_a_mantenimiento:
#             message += f"Unidad: {unidad['unidad__nombre']} - Kilometraje: {unidad['total_km']} km\n"
        
#         recipient_list = ['forniteb6@gmail.com']  # Reemplaza con el correo deseado
#         send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

#     return render(request, 'vista_kilometraje.html', {'unidades_km': unidades_km})
