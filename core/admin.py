from django.contrib import admin
from .models import Service, Education, Experience, Sobre, Endereco, Competencia, HeaderPicture, Skill,\
                    FiltrosProjetos, Projetos, Curriculo

from modeltranslation.admin import TranslationAdmin, TranslationTabularInline


admin.site.site_header = 'Administração de dados'
admin.site.site_title = 'Administração Currículo'
admin.site.index_title = 'Faça suas alterações aqui'


# Não vou traduzir o endereço/ sem necessidade
@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cidade', 'ativo', 'modificado')


# Não precisa traduzir só possui uma imagem
@admin.register(HeaderPicture)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('foto', 'ativo', 'modificado')


# Não precisa traduzir, só tem o gráfico e os programas
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('nome', 'porcentagem', 'ativo', 'modificado')


@admin.register(Education)
class EducationAdmin(TranslationAdmin):
    model = Education
    list_display = ('titulo', 'subtitulo', 'ativo', 'modificado')


@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    model = Service
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Experience)
class ExperienceAdmin(TranslationAdmin):
    model = Experience
    list_display = ('titulo', 'subtitulo', 'ativo', 'modificado')


@admin.register(Sobre)
class SobreAdmin(TranslationAdmin):
    model = Sobre
    list_display = ('nome', 'ativo', 'modificado')


@admin.register(Competencia)
class CompetenciaAdmin(TranslationAdmin):
    model = Competencia
    list_display = ('competencia', 'ativo', 'modificado')


@admin.register(FiltrosProjetos)
class FiltrosProjetosAdmin(TranslationAdmin):
    model = FiltrosProjetos
    list_display = ('nome', 'ativo', 'modificado')


@admin.register(Projetos)
class ProjetosAdmin(admin.ModelAdmin):
    model = Projetos
    list_display = ('nome', 'ativo', 'modificado')

@admin.register(Curriculo)
class CurriculoAdmin(admin.ModelAdmin):
    model = Curriculo
    list_display = ('titulo', 'arquivo_pdf', 'ativo', 'modificado')
