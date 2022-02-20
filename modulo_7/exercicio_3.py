# Implemente uma função maior_idade(pessoa) que receba uma tupla representando uma pessoa com nome e idade e imprime na tela se a pessoa é maior de idade ou não.

pessoaUm = ('paula', 17)
pessoaDois = ('leandro', 20)

def isAdult(pessoa):
  print(pessoa)
  if (pessoa[1] >= 18):
    return True

  return False

print(isAdult(pessoaUm))
print(isAdult(pessoaDois))