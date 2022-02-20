# Escreva uma função que recebe um número inteiro positivo e retorna True caso ele seja primo e False , caso contrário.

# numero primo - divisivel por 1 e por ele mesmo

def is_primo(number):
  count = 1
  countDiv = 0
  isPrimo = False

  while (count <= number):
    if (number % count == 0):
      countDiv = countDiv + 1
    count = count + 1

  if (countDiv <= 2):
    isPrimo = True

  return isPrimo

number = int(input('Digite um número: '))
print(is_primo(number))