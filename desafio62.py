pt = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razao: '))
termo = pt
c = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        c += 1
    print('Pausa')
    mais = int(input('Mais quantos deseja digitar?:'))
    print('total de termos foram:{}'.format(c))
