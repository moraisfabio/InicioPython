temp = list()
princ = list()
mai = men = 0
opcao = 0
while opcao != 'n':
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    opcao = str(input('Quer continuar? [S/N]').lower())
    princ.append(temp[:])
    temp.clear()
print(f'Ao todo voce, cadastrou {len(princ)} pessoas')
for p in princ:
    if p[1] == mai:
        print(f'O maior peso foi de {mai} Kg. de {p[0]}')
    if p[1] == men:
        print(f'O menor peso foi de {men} Kg. de {p[0]}')
