from django.core.validators import MinValueValidator, MaxValueValidator
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
        ('fa fa-2x fa-solid fa-robot service-icon bg-primary text-white mr-3', 'Robot'),
        ('fa fa-2x fa-solid fa-bolt service-icon bg-primary text-white mr-3', 'lightning'),

    )

    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=100, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Education(Base):

    titulo = models.CharField('Título', max_length=100)
    subtitulo = models.CharField('Subtítulo', max_length=100)
    inicio = models.IntegerField('Ano início', validators=[MinValueValidator(1900), MaxValueValidator(3000)])
    fim = models.IntegerField('Ano fim',  validators=[MinValueValidator(1900), MaxValueValidator(3000)])
    descricao = models.TextField('Descrição', max_length=200)

    class Meta:
        verbose_name = 'Educação'
        verbose_name_plural = 'Educação'

    def __str__(self):
        return self.titulo


class Experience(Education):

    class Meta:
        verbose_name = 'Experiência'
        verbose_name_plural = 'Experiências'
