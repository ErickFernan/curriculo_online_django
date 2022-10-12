from django.contrib import admin
from .models import Service, Education, Experience, Sobre, Endereco, Competencia, HeaderPicture, Skill,\
                    FiltrosProjetos, Projetos


admin.site.site_header = 'Administração de dados'
admin.site.site_title = 'Administração Currículo'
admin.site.index_title = 'Faça suas alterações aqui'


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


@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('competencia', 'ativo', 'modificado')


@admin.register(HeaderPicture)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('foto', 'ativo', 'modificado')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('nome', 'porcentagem', 'ativo', 'modificado')


@admin.register(FiltrosProjetos)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'modificado')


@admin.register(Projetos)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'modificado')

