from django.db import models
#
from django.contrib.auth.models import BaseUserManager
#


class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, email, password, is_staff, is_active, is_superuser, **extra_fields):
        user = self.model(
            email = email,
            is_staff = is_staff,
            is_active = is_active,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user



    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, False, **extra_fields)


    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, True, True, True, **extra_fields)



def codigo_valicacion(self, id_user, codigo_registro):
    if self.filter(id=id_user, codigo_registro=codigo_registro).exists():
        return True
    else:
        return False