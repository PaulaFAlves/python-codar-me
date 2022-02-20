# DESAFIO. Escreva um programa que dado uma lista de números inteiros, imprime o maior número dessa lista.

# lista = [1, 3, 2, 5]
# Deve imprimir 5

list = [1, 6, 10, 5]
listLength = len(list)
count = 0
maxNumber = 0

while (count < listLength):
  if (list[count] > maxNumber):
    maxNumber = list[count]
  count = count + 1

print(maxNumber)