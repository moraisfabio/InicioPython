print('='*25)
print('{:^30}'.format('BANCO FLO'))
print('='*25)
v = int(input('Qual valor voce deseja sacar? R$: '))
ced = 100
tot = v
totced = 0
while True:
    if tot >= ced:
        tot -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'O total de {totced} cedulas de R$ {ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 5
        elif ced == 5:
            ced = 1
        elif ced == 1:
            ced = 0
        totced = 0
        if tot == 0:
            break