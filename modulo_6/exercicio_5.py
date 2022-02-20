# Suponha o seguinte programa:

# Alunos e suas notas representados através de dicionários
# alunos = [
#   {
#     "nome": "Alice",
#     "nota": 8,
# }, {
#     "nome": "Bob",
# "nota": 7, },
#   {
#     "nome": "Carlos",
#     "nota": 9,
# } ]

# Escreva uma programa que calcula a média das notas de todos os alunos.

students = [
  {
    "nome": "Alice",
    "nota": 8,
}, {
    "nome": "Bob",
"nota": 7, },
  {
    "nome": "Carlos",
    "nota": 9,
} ]
studentsListLength = len(students)
count = 0
sum = 0
average = 0

while (count < studentsListLength):
  sum = sum + students[count]['nota']
  count = count + 1

average = sum / studentsListLength
print('A média das notas dos alunos é:', average)