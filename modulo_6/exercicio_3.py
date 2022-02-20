# Data uma lista de números inteiros, escreva um programa que calcula a média dos números na lista. O resultado não deve incluir números decimais. Exemplo: 12.3 deve imprimir apenas 12 .
# Se preferir, pode utilizar a lista abaixo como exemplo:

# lista = [1, 10, 20, 35, 22, 12]
# Resultado deve ser 16

list = [10, 20, 35, 22, 12]
listLength = len(list)
average = 0
sum = 0
count = 0 

while (count < listLength):
  sum = sum + list[count]
  count = count + 1

average = sum / listLength
print(int(average))