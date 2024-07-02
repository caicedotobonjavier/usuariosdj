from django.shortcuts import render
#
from .models import User
#
from django.views.generic import CreateView
#
from django.urls import reverse_lazy
# Create your views here.


class CrearUsuarioView(CreateView):
    template_name = 'users/crear-usuario.html'
    model = User
    fields = ['email', 'full_name','direccion','imagen','genero']
    success_url = reverse_lazy('users_app:crear_usuario')