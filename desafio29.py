velo = int(input('Informe a velocidade:'))

if velo > 80:
    print('Voce foi multado')
    valor =  velo%80 * 7
    print(' o valor da multa',valor)
