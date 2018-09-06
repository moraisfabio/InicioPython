import random
soma = c = 0
print('=--'*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=--'*15)
while True:
    jogador = int(input('Diga um valor: '))
    opcao = str(input('Par ou Impar(P / I):').upper())
    pc = random.randint(0, 10)
    print('-='*25)
    soma = jogador + pc
    print(f'Voce jogou {jogador} e o computador jogou {pc}. total deu {soma}')
    print('-='*25)
    if soma % 2 == 0 and opcao == 'P':
        print('VOCE VENCEU!!')
        print('Vamos Jogar novamente...')
    elif soma % 2 != 0 and opcao == 'I':
        print('VOCE VENCEU!!')
        print('Vamos Jogar novamente...')
    else:
        print('VOCE PERDEU!!')
        print('-='*25)
        break
    c += 1
(print(f'GAME OVER! Voce venceu {c} vezes.'))
