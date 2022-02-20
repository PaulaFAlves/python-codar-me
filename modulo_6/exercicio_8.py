# DESAFIO. Escreva um programa que declara uma lista com elementos de diferentes tipos e imprime na tela essa lista invertida. Não é permitido utilizar métodos como reverse ou sort .

list = [1, 2, 3, 4]
newList = []
listLength = len(list)
count = 1

while (count <= listLength):
  newList.append(list[listLength - count])
  count = count + 1

print(newList)