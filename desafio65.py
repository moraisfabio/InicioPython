n = 1
resp = 'S'
media = s = maior = menor = c = 0
while resp == 'S':
    n = int(input('Informe um valor:'))
    resp = str(input('Quer continuar?(S/N)').upper())
    c += 1
    s += n
    media = s / c
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('A media dos numeros digitados e:{} e o maior:{} e menor:{}'.format(media, maior, menor))