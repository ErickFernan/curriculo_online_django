from .models import Education

from modeltranslation.translator import TranslationOptions, register


@register(Education)
class EducationTranslationOptions(TranslationOptions):
    fields = ('titulo', 'subtitulo', 'descricao')
