from django.views.generic import TemplateView
from .models import Service, Experience, Education


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Service.objects.order_by('?').all()
        context['educacao'] = Education.objects.order_by('?').all()
        context['experiencia'] = Experience.objects.order_by('?').all()

        return context
