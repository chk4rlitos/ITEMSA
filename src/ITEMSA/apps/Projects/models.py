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
    tipodocumento = models.CharField(max_length=20, choices=constants.TIPO_DOCUMENTO_PERSONA, verbose_name="Tipo de Documento", null=True)
    documento = models.CharField(max_length=11, verbose_name="Documento")
    telefono_principal = models.CharField(max_length=10, verbose_name="N° Celular")
    telefono_secundario = models.CharField(max_length=10, verbose_name="N° Teléfono")
    email = models.EmailField(max_length=60,verbose_name="Correo Electrónico")
    fecha = models.DateField(auto_now=True, null=True)
    hora = models.TimeField(auto_now=True,  null=True)
    estado = models.BooleanField(default=False, verbose_name="¿Activo?")

    def save(self):
        super(Persona,self).save()

    def __unicode__(self):
        return str(self.apellidos +'-' + self.nombre)

    class Meta:
        app_label = 'Projects'
        ordering = ['apellidos']

class Personal(models.Model):
    persona = models.OneToOneField(Persona,on_delete=models.CASCADE,  unique=True)
    tipo_trabajador = models.CharField(max_length=20, choices=constants.TIPO_TRABAJADOR, verbose_name="Tipo de Trabajador", null=True)
    cargo = models.CharField(max_length=100,verbose_name="Cargo")
    fecha = models.DateField(auto_now=True, null=True)
    hora = models.TimeField(auto_now=True,  null=True)
    estado = models.BooleanField(default=False, verbose_name="¿Activo?")
    
    def __unicode__(self):
        return str(self.persona)

    class Meta:
        ordering = ['tipo_trabajador']

class PersonalUsuario(models.Model):
    usuariopersonal = models.OneToOneField(User,on_delete=models.CASCADE, unique=True)
    fecha = models.DateField(auto_now=True, null=True)
    hora = models.TimeField(auto_now=True,  null=True)
    estado = models.BooleanField(default=False, verbose_name="¿Activo?")

    def __unicode__(self):
        return str(self.usuariopersonal)

    class Meta:
        verbose_name = "Personal de Usuario"
        verbose_name_plural = "Personal de Usuarios"