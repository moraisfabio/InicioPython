total = cont = menor = 0
print('='*25)
print('SUPER LOJAO BARATAO')
print('='*25)
while True:
    prod = str(input('Nome do Produto: '))
    pre = float(input('Preco: '))
    op = str(input('Quer continuar?(S/N):').upper())
    total += pre
    if op == 'S':
        op
    if pre > 1000:
        cont += 1
    if pre < menor:
        menor = pre
    if op == 'N':
        break

print(f'O total da compra foi R${total} \nTemos {cont} produtos custando mais de R$1000,00 \nO produto mais barato foi {prod} que custa R${pre}')