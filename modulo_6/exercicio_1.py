# Escreva um programa que lê números inteiros positivos do usuário, um após o outro, e monta uma lista a partir desses números e depois imprime a lista montada. O programa deve continuar solicitando por números até que o elemento digitado seja um número negativo (que não deve ser inserido na lista).

isNumberNegative = False
numbersList = []

while (not isNumberNegative):
  number = int(input('Digite um número: '))

  if (number < 0):
    print('Número negativo!')
    isNumberNegative = True
    break

  numbersList.append(number)

