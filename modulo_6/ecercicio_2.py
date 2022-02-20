# Dada uma lista de números inteiros, escreva um programa que calcula a soma de todos os números na lista.
# Se preferir, pode utilizar a lista abaixo como exemplo:
# lista = [1, 10, 20, 35, 22, 12]
# Resultado deve ser = 100

list = [1, 20, 35, 22, 12]
count = 0
sum = 0

while (count < len(list)):
  sum = sum + list[count]
  count = count + 1

print(sum)
