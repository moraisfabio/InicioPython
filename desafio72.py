n = int(input('Digite um numero de 0 a 20:'))
tup = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete',
        'dezoito', 'dezenove', 'vinte')
while True:
    if n > 20:
        n = int(input('Tente novamente. Digite um numero entre 0 a 20:'))
    else:
        print(f'Voce digitou o numero {tup[n]}')
        break