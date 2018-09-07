sexo = 1
while sexo != 'F' or 'M':
    sexo = str(input('Informe o seu sexo:').upper())
    if sexo == 'F' or sexo == 'M':
        print('Obrigado por digitar o seu sexo.')
        break
print('Fim')
