lista = list()
opcao = 0
while opcao != 'n':
   lista.append(int(input('Informe um valor: ')))
   print('Valor adicionado com sucesso...')
   opcao = str(input('Deseja continuar?[S/N]: ').lower())
if 5 in lista:
   print('O valor 5 faz parte da lista...')
else:
   print('O valor 5 nao faz parte da lista..')
print(f'Voce digitou os valores {lista}')
print(f'O total de numeros digitados foram {len(lista)}')
print(f'Os valores da lista em decrescente: {sorted(lista, reverse=True)}')