from usuario import Usuario

class Administrador(Usuario):
  def imprimi_usuario(self):
    print(f'{self.nome} ({self.email}) -  Administrador')

