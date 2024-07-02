from django import forms
#
from .models import User
#
from django.contrib.auth import authenticate
#



class UserFomulario(forms.ModelForm):
    password1 = forms.CharField(
        required=True,
        label='Contraseña',
        widget= forms.PasswordInput(
            attrs={
                'placeholder' : 'Ingrese contraseña'
            }
        )
    )

    password2 = forms.CharField(
        required=True,
        label='Contraseña',
        widget= forms.PasswordInput(
            attrs={
                'placeholder' : 'Confirmar contraseña'
            }
        )
    )



    class Meta:
        model = User
        fields = (
            'email', 
            'full_name',
            'direccion',
            'genero',
            'imagen',
            
        )

        widgets = {
            'email' : forms.EmailInput(
                attrs={
                    'placeholder' : 'Correo Electronico'
                }
            ),

            'full_name' : forms.TextInput(
                attrs={
                    'placeholder' : 'Nombre Completo'
                }
            ),

            'direccion' : forms.TextInput(
                attrs={
                    'placeholder' : 'Direccion Domicilio'
                }
            ),
        }


    def clean_password2(self):
        password2 = self.cleaned_data['password2']
        if password2 != self.cleaned_data['password1']:
            raise forms.ValidationError('Las contraseñas no coinciden')
        
        return password2



class LoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        label='Correo Electronico',
        widget= forms.EmailInput(
            attrs={
                'placeholder' : 'Correo Electronico'
            }
        )
    )

    password = forms.CharField(
        required=True,
        label='Contraseña',
        widget= forms.PasswordInput(
            attrs={
                'placeholder' : 'Contraseña'
            }
        )
    )

    #validacion si se realizo o no autenticacion y login
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('El correo electronico o la contraseña son erroneos')
        
        return self.cleaned_data



class UpdatePasswordForm(forms.Form):
    password1 = forms.CharField(
        required=True,
        label= 'Contraseña Actual',
        widget= forms.PasswordInput(
            attrs={
                'placeholder' : 'Contraseña actual'
            }
        )
    )

    password2 = forms.CharField(
        required=True,
        label= 'Nueva Contraseña',
        widget= forms.PasswordInput(
            attrs={
                'placeholder' : 'Nueva Contraseña'
            }
        )
    )

    #al inicializar el paso el user capturado en las vistas, para usar el request que le doy el valor de user
    def __init__(self, user, *args, **kwargs):     
        self.request = user
        super(UpdatePasswordForm, self).__init__(*args, **kwargs)


    def clean(self):
        cleaned_data = super(UpdatePasswordForm, self).clean()

        usuario = self.request
        password1 = self.cleaned_data['password1']
        
        if not authenticate(email=usuario, password=password1):
            raise forms.ValidationError('Contraseña Actual Erronea')
        
        return self.cleaned_data


class UpdateInfoUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'full_name',
            'direccion',
            'imagen',
            'genero',
        )