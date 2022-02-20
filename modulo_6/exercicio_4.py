# Suponha o seguinte programa:
# Alunos e suas respectivas notas
# alunos = [
#  ("Alice", 8),
#  ("Bob", 7),
#  ("Carlos", 9),
# ]
# Escreva uma programa que calcula a média das notas de todos os alunos.


students = [
  ("Alice", 8),
  ("Bob", 7),
  ("Carlos", 9),
]
studentsListLength = len(students)
count = 0
sum = 0
average = 0

while (count < studentsListLength):
  sum = sum + students[count][1]
  count = count + 1

average = sum / studentsListLength
print('A média das notas dos alunos foi:', average)
