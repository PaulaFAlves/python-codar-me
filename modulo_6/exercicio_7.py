# Uma string ( str ) também pode ser percorrida utilizando o for .
# Escreva um programa que solicite uma string para o usuário e imprima quantas vezes cada letra aparece na palavra. Por exemplo:
# "banana"
# O resultado deve ser
# {
#    'a': 3,
#    'b': 1,


word = input('Digite uma palavra: ')
wordLength = len(word)
letterCounter = {}

letters = set(word)

for letter in letters:
  sum = 0
  count = 0 

  while (count < wordLength):
    if (letter == word[count]):
      sum = sum + 1
      
    count = count + 1
    
  letterCounter[letter] = sum

print(letterCounter)