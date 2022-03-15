from django.test import TestCase, Client
from agenda.models import Categoria, Evento
from datetime import date

class TestPaginaInicial(TestCase):
  def test_lista_eventos(self):
    client = Client()
    response = client.get('/')

    self.assertTemplateUsed(response, 'agenda/listar_eventos.html')

class TestListagemDeEventos(TestCase):
  def test_evento_com_data_de_hoje_exibido(self):
    categoria = Categoria()
    categoria.name = 'Backend'
    categoria.save()

    evento = Evento()
    evento.nome = 'Curso de JS'
    evento.categoria = categoria
    evento.local = 'São Paulo'
    evento.data = date.today()
    evento.save()

    client = Client()
    response = client.get('/')

    self.assertContains(response, 'Curso de JS')
    self.assertEqual(response.context['eventos'][0], evento)

  def test_eventos_sem_data_sao_exibidos(self):
    categoria = Categoria()
    categoria.name = 'Backend'
    categoria.save()

    evento = Evento()
    evento.nome = 'Curso de JS'
    evento.categoria = categoria
    evento.local = 'São Paulo'
    evento.data = None
    evento.save()

    client = Client()
    response = client.get('/')

    print(response.context['eventos'][0])

    self.assertContains(response, 'Curso de JS')
    self.assertContains(response, 'A definir')
    self.assertEqual(response.context['eventos'][0], evento)

