# exercicio 1

numberA = int(input('Digite um numero: '))

if (numberA % 3) == 0 and (numberA % 5) == 0:
  print('FizzBuzz')
elif (numberA % 3) == 0:
  print('Fizz')
elif (numberA % 5) == 0:
  print('Buzz')
else:
  print('N/A')


# exercicio 2

numberA = int(input('Digite um numero: '))
numberB = int(input('Digite outro numero: '))

op = input('Digite o operador: ')

if op == '+':
  print(numberA + numberB)
elif op == '-':
  print(numberA - numberB)
elif op == '*':
  print(numberA * numberB)
elif op == '/':
  if numberB == 0:
    print('Não é possível realizar divisão por zero!')
  else:
    print(numberA / numberB)
else:
  print('Operador invalido')

# exercicio 3

user = 'paula'
password = '1234'

userInput = input('Digite o nome do usuario: ') 
passwordInput = input('Digite a senha do usuario: ') 

if (userInput != user) and (passwordInput != password):
  print('Usuario e senha incorretos')
elif (userInput != user):
  print('Usuario nao existe')
elif (passwordInput != password):
  print('Senha incorreta')
else:
  print('Autenticacao bem sucedida')


