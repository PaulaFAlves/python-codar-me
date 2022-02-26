from usuario import Usuario
from administrador import Administrador

usuarioA = Usuario('Paula', 'paula@email.com')
usuarioB = Administrador('Leandro', 'leandro@email.com')

usuarioA.imprimi_usuario()
usuarioB.imprimi_usuario()
print(Usuario.quantidade)