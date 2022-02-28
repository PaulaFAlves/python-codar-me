from crypt import methods
from flask import Flask, abort, jsonify, make_response, request, json
from Evento import Evento
from EventoOnline import EventoOnline

app = Flask(__name__)

ev_online = EventoOnline("Live de Python")
ev2_online = EventoOnline("Live de JavaScript")
ev = Evento("Aula de Python", "Rio de Janeiro")

eventos = [ev_online, ev2_online, ev]

@app.route("/")
def index():
  return "<h1>Flask configurado com sucesso!</h1>"

@app.errorhandler(404)
def nao_encontrado(erro):
  return (jsonify(erro=str(erro)), 404)

@app.errorhandler(400)
def nao_encontrado(erro):
  return (jsonify(erro=str(erro)), 400)

@app.route("/api/eventos/")
def listar_eventos():
  eventos_dict = []
  for ev in eventos:
    eventos_dict.append(ev.__dict__)
  return jsonify(eventos_dict)

@app.route("/api/eventos/", methods=["POST"])
def criar_evento():
  data = json.loads(request.data)
  nome = data.get("nome")
  local = data.get("local")

  if not nome:
    abort(400, 'Nome do evento deve ser informado.')

  if local:
    evento = Evento(nome=nome, local=local)
  else:
    evento = EventoOnline(nome=nome)

  eventos.append(evento)

  return {
    "id": evento.id,
    "url": f'/api/eventos/{evento.id}/'
  }

def get_evento(id):
  for ev in eventos:
    if ev.id == id:
      return ev
      
  abort(404, "Evento não encontrado")
    
  

@app.route("/api/eventos/<int:id>/")
def detalhar_evento(id):
  ev = get_evento(id)
  return jsonify(ev.__dict__)

@app.route("/api/eventos/<int:id>/", methods=["DELETE"])
def deletar_evento(id):
  ev = get_evento(id)
  eventos.remove(ev)
  return jsonify(ev.__dict__)

@app.route("/api/eventos/<int:id>/", methods=["PUT"])
def editar_evento(id):
  data = request.get_json()
  nome = data.get("nome")
  local = data.get("local")

  if not nome:
    abort(400, 'Nome deve ser informado.')

  if not local:
    abort(400, 'Local deve ser informado.')

  ev = get_evento(id)

  ev.nome = nome
  ev.local = local

  return jsonify(ev.__dict__)

@app.route("/api/eventos/<int:id>/", methods=["PATCH"])
def editar_evento_parcial(id):
  data = request.get_json()
  ev = get_evento(id)

  if "nome" in data.keys():
    nome = data.get("nome")
    if not nome:
      abort(400, 'Local deve ser informado.')
    ev.nome = nome

  if "local" in data.keys():
    local = data.get("local")
    if not local:
      abort(400, 'Local deve ser informado.')
    ev.local = local

  return jsonify(ev.__dict__)


  