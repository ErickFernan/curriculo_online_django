from django.db import models
from stdimage.models import StdImageField


class Base(models.Model):
    criados = models.DateField('Criado', auto_now_add=True)
    modificado = models.DateField('Atualizado', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Service(Base):
    ICONE_CHOICES = (
        ('fa fa-2x fa-laptop service-icon bg-primary text-white mr-3', 'Laptop'),
        ('fa fa-2x fa-laptop-code service-icon bg-primary text-white mr-3', 'Laptop-code'),
        ('fab fa-2x fa-android service-icon bg-primary text-white mr-3', 'Android'),
        ('fab fa-2x fa-apple service-icon bg-primary text-white mr-3', 'Apple'),
        ('fa fa-2x fa-search service-icon bg-primary text-white mr-3', 'Search'),
        ('fa fa-2x fa-edit service-icon bg-primary text-white mr-3', 'Edit'),
    )

    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=100, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico
