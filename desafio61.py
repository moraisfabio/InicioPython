pt = int(input('Informe o primeiro termo da PA:'))
razao = int(input('Informe a razao da PA:'))
termo = pt
c = 1
while c <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    c += 1



print('FIM')