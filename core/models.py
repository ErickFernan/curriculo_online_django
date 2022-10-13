from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from stdimage import StdImageField

import uuid


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField(_('Criado'), auto_now_add=True)
    modificado = models.DateField(_('Atualizado'), auto_now=True)
    ativo = models.BooleanField(_('Ativo?'), default=True)

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

    servico = models.CharField(_('Serviço'), max_length=100)
    descricao = models.TextField(_('Descrição'), max_length=200)
    icone = models.CharField(_('Icone'), max_length=100, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = _('Serviço')
        verbose_name_plural = _('Serviços')

    def __str__(self):
        return self.servico


class Education(Base):

    titulo = models.CharField(_('Título'), max_length=100)
    subtitulo = models.CharField(_('Subtítulo'), max_length=100)
    inicio = models.IntegerField(_('Ano início'), validators=[MinValueValidator(1900), MaxValueValidator(3000)])
    fim = models.IntegerField(_('Ano fim'),  validators=[MinValueValidator(1900), MaxValueValidator(3000)])
    descricao = models.TextField(_('Descrição'), max_length=200)

    class Meta:
        verbose_name = _('Educação')
        verbose_name_plural = _('Educação')

    def __str__(self):
        return self.titulo


class Experience(Base):
    titulo = models.CharField(_('Título'), max_length=100)
    subtitulo = models.CharField(_('Subtítulo'), max_length=100)
    inicio = models.IntegerField(_('Ano início'), validators=[MinValueValidator(1900), MaxValueValidator(3000)])
    fim = models.IntegerField(_('Ano fim'), validators=[MinValueValidator(1900), MaxValueValidator(3000)])
    descricao = models.TextField(_('Descrição'), max_length=200)

    class Meta:
        verbose_name = _('Experiência')
        verbose_name_plural = _('Experiências')

    def __str__(self):
        return self.titulo


class Endereco(Base):
    pais = models.CharField(_('País'), max_length=15)
    estado = models.CharField(_('Estado'), max_length=15)
    cidade = models.CharField(_('Cidade'), max_length=20)

    class Meta:
        verbose_name = _('Endereço')
        verbose_name_plural = _('Endereço')

    def __str__(self):
        return self.cidade


class Sobre(Base):
    titulo = models.CharField(_('Título'), max_length=100)
    descricao = models.TextField(_('Descrição'), max_length=200)
    nome = models.CharField(_('Nome'), max_length=40)
    escolaridade = models.TextField(_('Escolariade'), max_length=45)
    telefone = models.CharField(_('Telefone'), max_length=20)
    endereco = models.ForeignKey('core.Endereco', verbose_name=_('Endereço'), on_delete=models.CASCADE)
    nascimento = models.DateField(_('Nascimento'))
    # experia_anos = models.CharField('Experiência', max_length=10)
    email = models.EmailField(max_length=254)
    # freelance = models.CharField('Freelance', max_length=15)
    imagem = StdImageField(_('Imagem'), upload_to=get_file_path,
                           variations={'thumb': {'width': 600, 'height': 600, 'crop': True}})

    class Meta:
        verbose_name = _('Sobre')
        verbose_name_plural = _('Sobre')

    def __str__(self):
        return self.titulo


class Competencia(Base):
    competencia = models.CharField(_('Competência'), max_length=40)

    class Meta:
        verbose_name = _('Competência')
        verbose_name_plural = _('Competências')

    def __str__(self):
        return self.competencia


class HeaderPicture(Base):
    foto = StdImageField(_('Imagem'), upload_to=get_file_path,
                         variations={'thumb': {'width': 600, 'height': 600, 'crop': True}})

    class Meta:
        verbose_name = _('Foto Header')
        verbose_name_plural = _('Fotos Header')

    def __str__(self):
        return f'{self.foto}'


class Skill(Base):
    BAR_CHOICES = (
        ('progress-bar bg-primary', _('Verde')),
        ('progress-bar bg-warning', _('Amarelo')),
        ('progress-bar bg-danger', _('Vermelho')),
        ('progress-bar bg-dark', _('Preto')),
        ('progress-bar bg-info', _('Azul')),
    )

    nome = models.CharField(_('Nome'), max_length=50)
    porcentagem = models.IntegerField(_('Porcentagem'), validators=[MinValueValidator(0), MaxValueValidator(100)])
    cor = models.CharField(_('Cor'), max_length=100, choices=BAR_CHOICES)
    
    class Meta:
        verbose_name = _('Habilidade')
        verbose_name_plural = _('Habilidades')

    def __str__(self):
        return f'{self.nome}'


class FiltrosProjetos(Base):
    nome = models.CharField('Nome_filtro', max_length=30)

    class Meta:
        verbose_name = _('FiltroProjeto')
        verbose_name_plural = _('FiltrosProjeto')

    def __str__(self):
        return f'{self.nome}'


class Projetos(Base):
    nome = models.CharField(_('Nome'), max_length=50)
    tag = models.ManyToManyField(FiltrosProjetos)
    imagem = StdImageField(_('Imagem'), upload_to=get_file_path,
                           variations={'thumb': {'width': 400, 'height': 300, 'crop': True}})
    link = models.CharField(_('Link'), max_length=200)

    class Meta:
        verbose_name = _('Projeto')
        verbose_name_plural = _('Projetos')

    def __str__(self):
        return f'{self.nome}'
