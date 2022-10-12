from django.test import TestCase
from django.test import Client  # cria um navegador para exedcutar ações GET, POST ....import
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):

    def setUp(self):

        self.dados = {
            'nome': 'Teste',
            'email': 'emailteste@teste.com',
            'assunto': 'Meu assunto',
            'mensagem': 'Minha mensagem'
            }

        self.client = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEqual(request.status_code, 302)

    def test_form_invalid(self):  # Dados faltando para dar erro
        dados = {
            'nome': 'Teste',
            'email': 'emailteste@teste.com'
        }
        request = self.client.post(reverse_lazy('index'), data=dados)
        self.assertEqual(request.status_code, 200)
