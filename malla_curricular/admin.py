from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Facultad)
admin.site.register(Carrera)
@admin.register(Ciclo)
class CicloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'carrera')
    list_filter = ('carrera',)
    search_fields = ('nombre',)
    list_per_page = 10
    fieldsets = (
        ('Información del ciclo', {
            'fields': ('nombre',)
        }),
        ('Información de la carrera', {
            'fields': ('carrera',)
        }),
    )
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        for asignatura in Asignatura.objects.filter(carrera=obj.carrera):
            Asignatura.objects.create(
                nombre=asignatura.nombre,
                siglas=asignatura.siglas,
                ape=asignatura.ape,
                acd=asignatura.acd,
                pp=asignatura.pp,
                aa=asignatura.aa,
                carrera=obj.carrera,
                ciclo=obj
            )
        obj.save()
@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'siglas', 'ape', 'acd', 'pp', 'aa', 'ciclo')
    list_filter = ('carrera', 'ciclo')
    search_fields = ('nombre', 'siglas')
    list_per_page = 10
    fieldsets = (
        ('Información de la asignatura', {
            'fields': ('nombre', 'siglas', 'ape', 'acd', 'pp', 'aa')
        }),
        ('Información de la carrera y ciclo', {
            'fields': ('carrera', 'ciclo')
        }),
    )
    readonly_fields = ('ape', 'acd', 'pp', 'aa')
    def save_model(self, request, obj, form, change):
        obj.ape = obj.ape + obj.acd + obj.pp + obj.aa
        super().save_model(request, obj, form, change)