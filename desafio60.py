from math import factorial
'''
Usando o While para o calculo fatorial
n = int(input('Informe um valor:'))
c = n
f = 1
while c > 0:
     print('{}'.format(c), end='')
     print(' x ' if c > 1 else '=', end='')
     f *= c
     c -=1
print(f)'''
'''
Usando a biblioteca para calculo fatorial
n = int(input('Informe um numero:'))
fa = factorial(n)
print('O fatorial de {}: {}'.format(n, fa))'''

'''Usando o for para calculo fatorial'''
n = int(input('Informe um numero:'))
c = n
f = 1
for c in range(n, 1, -1):
    if c > 1:
        f *= c
print('O valor e:{}'.format(f))

