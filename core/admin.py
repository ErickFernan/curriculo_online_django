from django.contrib import admin
from .models import Service, Education, Experience


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'ativo', 'modificado')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'ativo', 'modificado')