
valor = int(input('Digite um valor para fazermos a taboada:'))
for c in range(1, 11):
    print('{} * {} = {}'.format(valor, c, valor*c))
print('{:-^10}'.format('FIM'))
for i in range(1, 11):
    print('{} + {} = {}'.format(valor, i, valor + i))
print('{:-^10}'.format('FIM'))
for j in range(1, 11):
    print('{} - {} = {}'.format(valor, j, valor - j))
print('{:-^10}'.format('FIM'))
for f in range(1, 11):
    print('{} / {} = {}'.format(valor, f, valor / f))
print('{:-^10}'.format('FIM'))