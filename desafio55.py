maior = 0
menor = 1000
for c in range(0, 5):
    peso = float(input('Infore o seu peso:'))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print('O peso maior e:{} e o menor e:{}'.format(maior, menor))

