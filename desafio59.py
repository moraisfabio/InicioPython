v1 = 0
v2 = 0
menu = 0
v1 = int(input('Informe um numero:'))
v2 = int(input('Informe outro numero:'))
print('---Menu--- \n[1] Somar \n[2]Multiplicar \n[3]Maior \n[4]Novos numeros \n[5] Sair.')
while menu != 5:
    menu = int(input('Esolha uma opcao.'))
    if menu == 1:
        somar = v1 + v2
        print('A soma de {} + {}:{}'.format(v1, v2, somar))
    if menu == 2:
        mult = v1 * v2
        print('A multiplicacao de {} + {}:{}'.format(v1, v2, mult))
    if menu == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('O valor maior entre {} e {} e:{}'.format(v1, v2, maior))
    if menu == 4:
        print('Digite novos numeros:')
        v1 = int(input('Informe um numero:'))
        v2 = int(input('Informe outro numero:'))
    if menu == 5:
        print('Obrigado!')
