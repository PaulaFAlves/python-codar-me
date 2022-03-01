from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse

from agenda.models import Categoria, Evento

from datetime import date


# Create your views here.
def listar_eventos(request):
  #buscar eventos no banco
  eventos = Evento.objects.filter(data__gte=date.today())
  #exibir um template listando eventos
  return render(request=request, context={"eventos": eventos}, template_name="agenda/listar_eventos.html")

def exibir_evento(request, id):
  evento = get_object_or_404(Evento, id=id)

  return render(request=request, context={"evento": evento}, template_name="agenda/exibir_evento.html")


def participar_evento(request):
  evento_id = request.POST.get("evento_id")
  evento = get_object_or_404(Evento, id=evento_id)
  evento.participantes += 1
  evento.save()

  return HttpResponseRedirect(reverse('exibir_evento', args=(evento_id,)))

def listar_categorias(request):
  #buscar eventos no banco
  categorias = Categoria.objects.all()
  #exibir um template listando eventos
  return render(request=request, context={"categorias": categorias}, template_name="agenda/listar_categorias.html")
  
def exibir_categoria(request, id):
  categoria = get_object_or_404(Categoria, id=id)

  return render(request=request, context={"categoria": categoria}, template_name="agenda/exibir_categoria.html")