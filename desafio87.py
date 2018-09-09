matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
s = scol = slin = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posicao [{l},{c}]:'))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c] % 2 == 0:
            s += matriz[l][c]
    print()
print('-='*30)
print(f'A soma dos valores pares: {s}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma da 3 coluna: {scol}')
for c in range(0, 3):
    if c == 0:
        slin = matriz[1][c]
    elif matriz[1][c] > slin:
        slin = matriz[1][c]
print(f'O maior da segunda linha: {slin}')