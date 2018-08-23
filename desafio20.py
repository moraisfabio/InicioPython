import random

nome1 = input('Informe o seu nome: ')
nome2 = input('Informe o seu nome: ')
nome3 = input('Informe o seu nome: ')
nome4 = input('Informe o seu nome: ')

nomes = random.sample({nome1, nome2, nome3, nome4}, k=4)

print('A sequencia de alunos para a apresentacao e: {}'.format((nomes)))

