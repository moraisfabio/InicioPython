lista = list()
maior = menor = 0
for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor para a Posicao {cont}:')))
print(f'Voce digitou os valores{lista}')
print(f'O maior valor digitado foi {max(lista)} nas posicoes ', end='')
print(f'\nO menor valor digitado foi {min(lista)} nas posicoes ', end='')
for c in range(5):
    if lista[c] == max(lista):
        print(f'{c}', end='')
    if lista[c] == min(lista):
        print(f'{c}', end='')
