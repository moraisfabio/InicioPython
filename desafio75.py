num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero')),
       int(input('Digite o ultimo numero:')))
print(f'Voce digitou os valores {num}')
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 aparaceu na {num.index(3)+1}ª posiçao')
else:
    print(f'O numero 3 nao foi digitado em nenhuma posicao')
print(f'Os valores pares foram:', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
