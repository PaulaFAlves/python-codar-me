#  Implemente uma função que recebe dois argumentos, uma lista e um elemento , e retorna True caso elemento seja encontrado na lista , e False caso contrário. Não é permitido utilizar o método in .


list = [1,2,3,4]
element = 12
listLength = len(list)

def check_element(list):
  count = 0 
  itHasElement = False

  while (count < listLength):
    if (list[count] == element):
      itHasElement = True
    count = count + 1

  return itHasElement

print(check_element(list))
    
