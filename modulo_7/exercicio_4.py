# Adapte a função maior_idade(pessoa) de forma que ela possa receber tanto uma tupla quanto um dicionário. Dica: método type pode te ajudar.

pessoaTupla = ('paula', 17)
pessoaDict = {'name':'leandro', 'idade': 20}

def isAdult(pessoa):
  if (type(pessoa) == tuple):
    if (pessoa[1] >= 18):
      return True
    return False
  
  if (pessoa['idade'] >= 18):
    return True
  return False

print(isAdult(pessoaTupla))
print(isAdult(pessoaDict))