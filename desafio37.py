num = int(input('Informe um numero: '))
print('Esolha uma base para transformar: \nBinario = 1 \nOctal = 2 \nHexadecimal = 3')
opcao = int(input())
if opcao == 1:
    binario = bin(num)
    print('O valor transformado em Binario:{}'.format(binario))
elif opcao == 2:
    octal = oct(num)
    print('O valor transformado em Octal:{}'.format(octal))
elif opcao == 3:
    Hexadecimal = hex(num)
    print('O valor em base decimal:{}'.format(Hexadecimal))

