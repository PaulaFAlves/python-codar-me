from django.db import models

# Create your models here.
class Categoria(models.Model):
  nome = models.CharField(max_length=256, unique=True)

  def __str__(self): # para formatar a exibicao no admin do django
      return f"{self.nome} <{self.id}>"

  @classmethod
  def cria_categoria(cls, nome):
    if not nome:
      raise ValueError("Categoria precisa de nome")

    categoria = Categoria(nome=nome)

    categoria.save()

    return categoria

class Evento(models.Model):
  nome = models.CharField(max_length=256)
  categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
  local = models.CharField(max_length=256, blank=True)
  link = models.CharField(max_length=256, blank=True)
  data = models.DateField(null=True)
  participantes = models.IntegerField(default=0)

  def __str__(self):
      return f"{self.nome} <{self.id}>"

  @classmethod
  def cria_evento(cls, nome, categoria, local=None, link=None, data=None):
    if not nome:
      raise ValueError("Evento precisa de nome")

    if not categoria:
      raise ValueError("Evento precisa de categoria")

    if local and link:
      raise ValueError('O evento não pode ter um local e um link.')

    if local and data:
      evento = Evento(nome=nome, categoria=categoria, local=local, data=data)
    elif link and data:
      evento = Evento(nome=nome, categoria=categoria, link=link, data=data)
    elif local:
      evento = Evento(nome=nome, categoria=categoria, local=local)
    elif link:
      evento = Evento(nome=nome, categoria=categoria, link=link)
    else:
      evento = Evento(nome=nome, categoria=categoria)

    evento.save()

    return evento

