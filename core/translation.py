from .models import Education, Service, Experience, Sobre, Competencia, FiltrosProjetos, Projetos

from modeltranslation.translator import TranslationOptions, register


@register(Education)
class EducationTranslationOptions(TranslationOptions):
    fields = ('titulo', 'subtitulo', 'descricao')


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('servico', 'descricao')


@register(Experience)
class ExperienceTranslationOpions(TranslationOptions):
    fields = ('titulo', 'subtitulo', 'descricao')


@register(Sobre)
class SobreTranslationOpions(TranslationOptions):
    fields = ('titulo', 'descricao', 'escolaridade')


@register(Competencia)
class CompetenciaTranslationOpions(TranslationOptions):
    fields = ('competencia',)


@register(FiltrosProjetos)
class FiltrosProjetoTranslationOpions(TranslationOptions):
    fields = ('nome',)


@register(Projetos)
class ProjetosTranslationOpions(TranslationOptions):
    fields = ('nome',)
