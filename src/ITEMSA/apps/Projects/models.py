from django.db import models
from django.template import Context
from django.conf import settings
from django.template.loader import get_template
from django.contrib.auth.models import User
from . import constants
from django.template import defaultfilters


class Persona(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombres", null=True)
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos", null=True)
    direccion = models.CharField(max_length=200, verbose_name="Direccion", null=True)
    tipodocumento = models.CharField(max_length=20, choices=constants.TIPO_DOCUMENTO_PERSONA, verbose_name="Tipo de Documento", null=True)
    documento = models.CharField(max_length=11, verbose_name="Documento")
    estado_civil = models.CharField(max_length=20, choices=constants.ESTADO_CIVIL, verbose_name="Estado Civil", null=True)
    telefono_principal = models.CharField(max_length=10, verbose_name="N° Celular")
    telefono_secundario = models.CharField(max_length=10, verbose_name="N° Teléfono", blank=True)
    email = models.EmailField(max_length=60,verbose_name="Correo Electrónico")
    fecha = models.DateField(auto_now=True, null=True)
    hora = models.TimeField(auto_now=True,  null=True)
    estado = models.BooleanField(default=True, verbose_name="¿Activo?")

    def save(self):
        super(Persona,self).save()

    def __str__(self):
        return str(self.apellidos + ',' + self.nombre)

    class Meta:
        app_label = 'Projects'
        ordering = ['apellidos']

class Personal(models.Model):
    persona = models.OneToOneField(Persona,on_delete=models.CASCADE,  unique=True)
    tipo_trabajador = models.CharField(max_length=20, choices=constants.TIPO_TRABAJADOR, verbose_name="Tipo de Trabajador", null=True)
    cargo = models.CharField(max_length=100,verbose_name="Cargo")
    fecha = models.DateField(auto_now=True, null=True)
    hora = models.TimeField(auto_now=True,  null=True)
    estado = models.BooleanField(default=True, verbose_name="¿Activo?")
    
    def __str__(self):
        return str(self.persona)

    class Meta:
        ordering = ['tipo_trabajador']
        verbose_name = "Personal"
        verbose_name_plural = "Personal"

class PersonalUsuario(models.Model):
    usuariopersonal = models.OneToOneField(User,on_delete=models.CASCADE, unique=True, verbose_name="Usuario")
    personal = models.OneToOneField(Personal,on_delete=models.CASCADE, unique=True, verbose_name="Personal")
    fecha = models.DateField(auto_now=True, null=True)
    hora = models.TimeField(auto_now=True,  null=True)
    estado = models.BooleanField(default=True, verbose_name="¿Activo?")

    def __str__(self):
        return str(self.usuariopersonal)

    class Meta:
        verbose_name = "Personal de Usuario"
        verbose_name_plural = "Personal de Usuarios"