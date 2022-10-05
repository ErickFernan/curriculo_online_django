from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from stdimage import StdImageField
import uuid


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


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


class Experience(Base):
    titulo = models.CharField('Título', max_length=100)
    subtitulo = models.CharField('Subtítulo', max_length=100)
    inicio = models.IntegerField('Ano início', validators=[MinValueValidator(1900), MaxValueValidator(3000)])
    fim = models.IntegerField('Ano fim', validators=[MinValueValidator(1900), MaxValueValidator(3000)])
    descricao = models.TextField('Descrição', max_length=200)

    class Meta:
        verbose_name = 'Experiência'
        verbose_name_plural = 'Experiências'

    def __str__(self):
        return self.titulo


class Endereco(Base):
    pais = models.CharField('País', max_length=15)
    estado = models.CharField('Estado', max_length=15)
    cidade = models.CharField('Cidade', max_length=20)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereço'

    def __str__(self):
        return self.cidade


class Sobre(Base):
    titulo = models.CharField('Título', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    nome = models.CharField('Nome', max_length=40)
    escolaridade = models.TextField('Escolariade', max_length=45)
    telefone = models.CharField('Telefone', max_length=20)
    endereco = models.ForeignKey('core.Endereco', verbose_name='Endereço', on_delete=models.CASCADE)
    nascimento = models.DateField('Nascimento')
    # experia_anos = models.CharField('Experiência', max_length=10)
    email = models.EmailField(max_length=254)
    # freelance = models.CharField('Freelance', max_length=15)
    imagem = StdImageField('Imagem', upload_to=get_file_path,
                           variations={'thumb': {'width': 600, 'height': 600, 'crop': True}})

    class Meta:
        verbose_name = 'Sobre'
        verbose_name_plural = 'Sobre'

    def __str__(self):
        return self.titulo


class Competencia(Base):
    competencia = models.CharField('Competência', max_length=40)

    class Meta:
        verbose_name = 'Competência'
        verbose_name_plural = 'Competências'

    def __str__(self):
        return self.competencia


class HeaderPicture(Base):
    foto = StdImageField('Imagem', upload_to=get_file_path,
                         variations={'thumb': {'width': 600, 'height': 600, 'crop': True}})

    class Meta:
        verbose_name = 'Foto Header'
        verbose_name_plural = 'Fotos Header'

    def __str__(self):
        return f'{self.foto}'


class Skill(Base):
    BAR_CHOICES = (
        ('progress-bar bg-primary', 'Verde'),
        ('progress-bar bg-warning', 'Amarelo'),
        ('progress-bar bg-danger', 'Vermelho'),
        ('progress-bar bg-dark', 'Preto'),
        ('progress-bar bg-info', 'Azul'),
    )

    nome = models.CharField('Nome', max_length=50)
    porcentagem = models.IntegerField('Porcentagem', validators=[MinValueValidator(0), MaxValueValidator(100)])
    cor = models.CharField('Cor', max_length=100, choices=BAR_CHOICES)
    
    class Meta:
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return f'{self.nome}'

    