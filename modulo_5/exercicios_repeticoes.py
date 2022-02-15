# exercicio 1

inputNumber = int(input('Digite um numero: '))
count = 0 
sum = 0 

while (count <= inputNumber):
  sum = sum + count
  count = count + 1

print('A soma de todos os números é:', sum)

# exercicio 2

inputNumber = int(input('Digite um numero: '))
count = 0

while (count <= inputNumber):
  if (count % 2 == 0):
    print(count)
  count = count + 1

# exercicio 3

inputNumber = int(input('Digite um numero: '))
count = 1
mult = 0

while (count <= inputNumber):
  if (inputNumber % count == 0):
    mult = mult + 1
  count = count + 1

if (mult <= 2):
  print('Este número é primo:', inputNumber)
else:
  print('Este número não é primo:', inputNumber)

# exercicio 4

misteriousNumber = 5
getItRight = False
numberOfMistakes = 0

while (not getItRight):
  if (numberOfMistakes >= 3):
    print('Suas chances acabaram!')
    break

  number = int(input('Digite um número'))

  if (number == misteriousNumber):
    print('Voce acertou')
    getItRight = True
  else:
    print('Voce errou!')

    if (number > misteriousNumber):
      print('O numero misterioso é menor que isso!')
    else:
      print('O numero misterioso é maior que isso!')

    numberOfMistakes = numberOfMistakes + 1