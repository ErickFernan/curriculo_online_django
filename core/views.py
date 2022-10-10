from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Service, Experience, Education, Sobre, HeaderPicture, Competencia, Skill, FiltrosProjetos, Projetos
from .forms import ContatoForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

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

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail.')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
