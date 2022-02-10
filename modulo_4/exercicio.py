# exercicio 1

number = input('digite um numero: ')
isEven = (int(number) % 2) == 0
print('O numero é par? ', isEven)

# exercicio 2

a=5
b = 10
x = True 
y = False
print((x or y) and (a < b)) 
# true
print((x or y) and not (a < b))
# false

# # exercicio 3

resultado = 2 + 3 * 2 ** 2
print(resultado)
# 14

resultado = 2 + (3 * 2) ** 2
print(resultado)
# 38

resultado = ((2 + 3) * 2) ** 2
print(resultado)
# 100

# exercicio 4

value = input('Digite o valor da compra: ')
freight = input('Digite o valor do frete: ')
isRegistered = input('O cliente é cadastrado no programa? (s/n)')

isAbleToApplyDiscount = (int(value) + int(freight)) > 100 or (isRegistered == 's')

print('Desconto pode ser aplicado? ', isAbleToApplyDiscount)


