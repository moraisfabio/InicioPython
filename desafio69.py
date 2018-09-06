tot = toth = totm = 0
print('='*25)
print('CADASTRE UMA PESSOA')
print('-'*25)
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ').upper())
    op = str(input('Quer continuar?(S / N):').upper())
    while op != 'S' and op != 'N':
        sexo = str(input('Sexo: ').upper())
    if idade > 18:
        tot += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm += 1
    if op == 'N':
        break
print(f'Total de pessoas com mais de 18 anos:{tot}\nAo todo temos {toth} homens cadastrados.\nE temos {totm} mulheres com menos de 20 anos.')




