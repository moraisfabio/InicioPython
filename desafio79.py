lista = list()
opcao = n = 0
while opcao != 'n':
    lista.append(int(input('Digite um numero: ')))
    print('Valor adicionado com sucesso...')
    opcao = str(input('Quer continuar?[S/N]: ').lower())
print('-='*30)
print(f'Voce digitou os valores {sorted(lista)}')

