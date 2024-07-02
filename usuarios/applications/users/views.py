from django.http import HttpResponse
#
from django.shortcuts import render
#
from .models import User
#
from django.views.generic import CreateView, FormView, View, UpdateView
#
from .forms import UserFomulario, LoginForm, UpdatePasswordForm
#
from django.contrib.auth import authenticate, login, logout
#
from django.urls import reverse_lazy, reverse
#
from django.http.response import HttpResponseRedirect
# Create your views here.


class CrearUsuarioView(FormView):
    template_name = 'users/crear-usuario.html'
    model = User
    #fields = ['email', 'full_name','direccion','imagen','genero']
    form_class = UserFomulario
    success_url = reverse_lazy('users_app:crear_usuario')


    def form_valid(self, form):

        User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            full_name = form.cleaned_data['full_name'],            
            direccion = form.cleaned_data['direccion'],
            genero = form.cleaned_data['genero'],
            imagen = form.cleaned_data['imagen'],
        )

        return super(CrearUsuarioView, self).form_valid(form)



class LoginUserView(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:index')


    def form_valid(self, form):
        usuario = form.cleaned_data['email']
        password = form.cleaned_data['password']

        user = authenticate(
            email=usuario, 
            password=password
        )

        login(self.request, user)

        return super(LoginUserView, self).form_valid(form)



class LogoutView(View):
    
    def get(self, request, *args, **kwargs):
        logout(request)

        return HttpResponseRedirect(
            reverse(
                'users_app:login_usuario'
            )
        )
    


class ActualizarPasswordView(FormView):
    template_name = 'users/update-password.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy(
        'users_app:login_usuario'
    )

    #intercepto los kwargs para pasarle al formulario el usuario, asi puedo usarlo en los forms
    def get_form_kwargs(self):
        kwargs = super(ActualizarPasswordView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


    def form_valid(self, form):
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']
        
        user = authenticate(email = self.request.user, password = password1)

        if user:
            usuario = self.request.user
            usuario.set_password(password2)
            usuario.save()
        logout(self.request)

        return super(ActualizarPasswordView, self).form_valid(form)
