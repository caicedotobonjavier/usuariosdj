from django.shortcuts import render
#
from django.views.generic import TemplateView

#importo el LoginRequiredMixin para que no se acceda a una vista sin estar logueado un usuarios
from django.contrib.auth.mixins import LoginRequiredMixin
#
from django.urls import reverse_lazy
# Create your views here.


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'home/index.html'
    #si el usuario no esta logueado se redirecciona al logueo
    login_url = reverse_lazy(
        'users_app:login_usuario'
    )