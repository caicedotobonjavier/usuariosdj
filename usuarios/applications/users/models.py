from django.db import models
#
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager
# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    """Modelo para los usuarios"""

    MASCULINO = '0'
    FEMENINO = '1'
    OTRO = '2'

    CHOICES_GENERO = (
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
        (OTRO, 'Otro')
    )

    email = models.EmailField('Correo Electronico', max_length=254, unique=True)
    full_name = models.CharField('Nombre Completo', max_length=50)
    direccion = models.CharField('Direccion Domicilio', max_length=50, blank=True, null=True)
    imagen = models.ImageField('Foto Perfil', upload_to='Usuarios',blank=True, null=True)
    genero = models.CharField('Genero', max_length=1, choices=CHOICES_GENERO, blank=True)
    #campo para la verificacion de usaurio con correo
    codigo_registro = models.CharField('Codigo Registro', max_length=6, blank=True)


    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']


    def __str__(self):
        return self.email