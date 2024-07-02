from django.urls import path, re_path, include
#
from . import views


app_name = 'users_app'

urlpatterns = [
    path('crear-usuario/', views.CrearUsuarioView.as_view(), name='crear_usuario'),
]