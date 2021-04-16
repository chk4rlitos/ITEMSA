from django.contrib import admin
from .models import Persona,Personal,PersonalUsuario
from django.contrib.admin import ModelAdmin

# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellidos', 'tipodocumento', 'documento','estado' ] 

class PersonalAdmin(admin.ModelAdmin):
    list_display = ['persona','tipo_trabajador', 'cargo', 'estado' ] 

admin.site.register(Persona,PersonaAdmin)
admin.site.register(Personal,PersonalAdmin)
admin.site.register(PersonalUsuario)