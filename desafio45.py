from random import  randint
print('-------Jokenpo--------'
      '\nVamos jogar:?'
      '\n1 = Sim'
      '\n2 = Nao')
pedra = 3
tesoura = 4
papel = 5
opcao = int(input(''))
if opcao == 1:
    print('Ecolha um? \n3 = Pedra \n4 = Tesoura \n5 = Papel')
    jogadorusr = int(input('Escolha:'))
    pc = randint(3, 5)
if pedra == jogadorusr and pedra == pc:
    print('Empate')
elif pedra == jogadorusr and tesoura == pc:
    print('voce ganhou!')
elif pedra == jogadorusr and papel == pc:
    print('Voce perdeu!')
elif tesoura == jogadorusr and tesoura == pc:
    print('Empate!')
elif tesoura == jogadorusr and pedra == pc:
    print('Voce perdeu!')
elif tesoura == jogadorusr and papel == pc:
    print('Voce Ganhou!')
elif papel == jogadorusr and papel == pc:
    print('Empate!')
elif papel == jogadorusr and pedra == pc:
    print('Voce Ganhou!')
elif papel == jogadorusr and tesoura == pc:
    print('Voce perdeu!')
else:
    print('Que pena, jogaremos na Proxima!')
print('Voce jogou:{} e o pc jogou:{}'.format(jogadorusr, pc))

