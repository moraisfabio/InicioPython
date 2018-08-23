import random
nome1 = input('Informe o seu nome: ')
nome2 = input('Informe o seu nome: ')
nome3 = input('Informe o seu nome: ')
nome4 = input('Informe o seu nome: ')
alunos = (nome1, nome2, nome3, nome4)
print('O aluno sorteado para apagar o quadro e: {}'.format(random.choice(alunos)))
