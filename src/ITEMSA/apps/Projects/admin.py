from django.contrib import admin
from .models import Persona,Personal,PersonalUsuario
from django.contrib.admin import ModelAdmin

# Register your models here.

admin.site.register(Persona)
admin.site.register(Personal)
admin.site.register(PersonalUsuario)