media = 0
s = 0
maior = 0
tot = 0
for c in range(1, 3):
    nome = str(input('Informe seu nome:'))
    idade = int(input('Informe a sua idade:'))
    sexo = str(input('Informe o seu sexo:'))
    s += idade
    media = s / 2
    if idade > maior and sexo == 'M':
        maior = idade
    if sexo == 'F' and idade < 20:
        tot += 1
print('O nome do Homem mais velho:{}'.format(nome))
print('O total de mulher com menos de 20 anos:{}'.format(tot))
print('A soma e:{} e a media:{}'.format(s, media))
