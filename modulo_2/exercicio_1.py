# exercício 1

string_variable = 'variável de string'
integer_variable = 12
float_variable = 12.3
bool_variable = False

print(type(string_variable))
print(type(integer_variable))
print(type(float_variable))
print(type(bool_variable))

# exercício 2

valor_compras = 12.25
desconto = 5.5
quantidade_itens = 2

total_das_compras = valor_compras * quantidade_itens
total_liquido_das_compras = total_das_compras * (1 - 5.5 / 100)

print(total_das_compras)
print(total_liquido_das_compras)

custo_medio_por_item = total_liquido_das_compras / quantidade_itens

print(custo_medio_por_item)