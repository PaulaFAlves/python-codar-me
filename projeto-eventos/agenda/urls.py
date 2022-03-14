from django.urls import path
from agenda.views import exibir_categoria, exibir_evento, listar_categorias, listar_eventos, participar_evento, exibir_categoria

urlpatterns = [
  path("", listar_eventos, name="listar_eventos_raiz"),
  path("eventos", listar_eventos, name="listar_eventos"),
  path("eventos/<int:id>/", exibir_evento, name="exibir_evento"),
  path("participar/", participar_evento, name="participar_evento"),
  path("categoria/<int:id>/", exibir_categoria, name="exibir_categoria"),
  path("categorias", listar_categorias, name="listar_categorias"),
]