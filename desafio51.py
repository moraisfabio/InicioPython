pt = int(input('Informe o primeiro termo da PA:'))
razao = int(input('Informe a razao da PA:'))
termo = pt
for c in range(pt, 10):
    print('{} -> '.format(termo),end='')
    termo += razao
print('FIM')
