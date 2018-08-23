s = 0
pri = int(input('Informe um numero inteiro:'))
for c in range(1, pri+1):
    if pri % c == 0:
        s += 1
if s == 2:
    print('Esse numero e primo.')
else:
    print('Esse numero nao e primo.')