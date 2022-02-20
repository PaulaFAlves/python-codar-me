# Implemente uma função que recebe uma lista de números inteiros e retorna uma tupla (pos, num) , onde pos é a posição (ou índice) do maior número na lista e num é o valor desse número.

def return_max_number(list):
  listLength = len(list)
  count = 0
  maxNumber = 0
  maxNumberPosition = 0

  while (count < listLength):
    if (list[count] > maxNumber):
      maxNumber = list[count]
      maxNumberPosition = count
    count = count + 1
  return (maxNumber, maxNumberPosition)

list = [2,4,8,7]
print(return_max_number(list))