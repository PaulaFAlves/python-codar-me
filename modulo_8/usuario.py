class Usuario:
  quantidade = 0 #atributo de classe

  def __init__(self, nome, email):
      self.nome = nome #atributos de instancia
      self.email = email
      self.quantidade = Usuario.quantidade
      Usuario.quantidade += 1

  # metodo de instancia
  def imprimi_usuario(self):
    print(f'{self.nome} ({self.email})')
