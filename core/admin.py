from django.contrib import admin
from .models import Service, Education, Experience, Sobre, Endereco


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'ativo', 'modificado')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'ativo', 'modificado')


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cidade', 'ativo', 'modificado')


@admin.register(Sobre)
class SobreAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'modificado')
