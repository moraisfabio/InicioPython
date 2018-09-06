print('Sequencia de Ficonacci')
print('-='*20)
n = int(input('Digite um valor: '))
c = 1
p1 = 0
p2 = 1
print('{} {} -> '.format(p1, p2),end='')
while c <= n:
    p3 = p1 + p2
    print('{} -> '.format(p3), end='')
    p1 = p2
    p2 = p3
    c += 1
print('Fim')
