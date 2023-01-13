import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path


class GetFilePathTestCase(TestCase):
    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))


class ServiceTestCase(TestCase):
    def setUp(self):
        self.servico = mommy.make('Service')


    def test_str(self):
        self.assertEquals(str(self.servico), self.servico.servico)


class EducationTestCase(TestCase):
    def setUp(self):
        self.titulo = mommy.make('Education')

    def test_str(self):
        self.assertEquals(str(self.titulo), self.titulo.titulo)


class ExperienceTestCase(TestCase):
    def setUp(self):
        self.titulo = mommy.make('Experience')

    def test_str(self):
        self.assertEquals(str(self.titulo), self.titulo.titulo)


class EnderecoTestCase(TestCase):
    def setUp(self):
        self.cidade = mommy.make('Endereco')

    def test_str(self):
        self.assertEquals(str(self.cidade), self.cidade.cidade)


class SobreTestCase(TestCase):
    def setUp(self):
        self.titulo = mommy.make('Sobre')

    def test_str(self):
        self.assertEquals(str(self.titulo), self.titulo.titulo)


class CompetenciaTestCase(TestCase):
    def setUp(self):
        self.competencia = mommy.make('Competencia')

    def test_str(self):
        self.assertEquals(str(self.competencia), self.competencia.competencia)


class HeaderPictureTestCase(TestCase):
    def setUp(self):
        self.foto = mommy.make('HeaderPicture')

    def test_str(self):
        self.assertEquals(str(self.foto), self.foto.foto)


class SkillTestCase(TestCase):
    def setUp(self):
        self.nome = mommy.make('Skill')

    def test_str(self):
        self.assertEquals(str(self.nome), self.nome.nome)


class FiltrosProjetosTestCase(TestCase):
    def setUp(self):
        self.nome = mommy.make('FiltrosProjetos')

    def test_str(self):
        self.assertEquals(str(self.nome), self.nome.nome)


class ProjetosTestCase(TestCase):
    def setUp(self):
        self.nome = mommy.make('Projetos')

    def test_str(self):
        self.assertEquals(str(self.nome), self.nome.nome)
