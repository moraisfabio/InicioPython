c = total = 0
print('condicao de flag com break')
print('-=:'*20)
while True:
    n = int(input('Informe um valor (999 para parar): '))
    if n == 999:
        break
    total += 1
    c += n
print(f'Total de numeros digitados:{total} com soma:{c}')
