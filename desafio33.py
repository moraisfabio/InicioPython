num1 = int(input('Informe um numero:'))
num2 = int(input('Informe outro numero:'))
num3 = int(input('Informe outro:'))

if num1 > num2:
    maior = num1
    menor = num2
else:
    maior = num2
    menor = num1
if num3 > maior:
    maior = num3
else:
    menor = num3

print('O numero maior e:{}, o menor e:{}'.format(maior, menor))

