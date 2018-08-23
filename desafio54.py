s = 0
d = 0
for c in range(0, 7):
    ano = int(input('Informe o seu ano de nascimento:'))
    total = 2018 - ano
    if total >= 21:
        s = s + 1
    if total < 21:
        d = d + 1

print('Ja atingiram a maior idade: {}'.format(s))
print('Ainda nao atingiram a maior idade:{}'.format(d))