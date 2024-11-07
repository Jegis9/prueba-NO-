from django.urls import path
from . import views


urlpatterns = [
# rutas de modulos para navegacion
    path('desactivar_usuario/<int:user_id>/', views.desactivar_usuario, name='desactivar_usuario'),
    path('desactivar_usuario_publico/<int:user_id>/', views.desactivar_usuario_publico, name='desactivar_usuario_publico'),
    path('lUsuarios/', views.lUsuarios, name='lUsuarios'),
    path('lInternos', views.lInternos, name='lInternos'),
    
  
]

