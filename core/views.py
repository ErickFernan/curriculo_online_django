from django.views.generic import TemplateView
from .models import Service, Experience, Education, Sobre, HeaderPicture, Competencia, Skill, FiltrosProjetos, Projetos


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Service.objects.order_by('?').all()
        context['educacao'] = Education.objects.all()
        context['experiencia'] = Experience.objects.all()
        context['sobre'] = Sobre.objects.all()
        context['picture'] = HeaderPicture.objects.all()
        context['competencia'] = Competencia.objects.order_by('?').all()
        context['habilidade'] = Skill.objects.order_by('?').all()
        context['filtros'] = FiltrosProjetos.objects.order_by('?').all()
        context['projetos'] = Projetos.objects.order_by('?').all()

        return context
