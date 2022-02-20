# DESAFIO. Uma função fatorial calcula o valor da multiplicação de um certo número inteiro não-negativo por todos os números positivos menores que ele. A exceção é o fatorial de zero que é igual a 1. 

def fatorial(number):
  result = 1
  count = 0

  if (number == 0) or (number == 1):
    result = 1

  while (count < number):
    result = result * (number - count)
    count = count + 1
  
  return result

number = 4
print(fatorial(number))

def fatorialDois(n):                             
    if n==0 or n == 1:                       
        return 1                             
    else:                                    
        fat = n * fatorial(n-1)              
    return fat                              

print(fatorialDois(4))