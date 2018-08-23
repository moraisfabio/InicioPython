produto = float(input('Informe o valor do produto:'))
print('-------MENU------- \nEscolha a forma de pagamento.'
      '\n1 - A vista ou no cheque.'
      '\n2 - Cartao'
      '\n3 - Parcelado em ate 2x Cartao'
      '\n4 - Parcelado em 3x ou mais Cartao.')
vista = 1
cartao = 2
par2x = 3
par3x = 4
opcao = int(input(''))
if opcao == 1:
    total = produto - produto * 0.10
    print('O valor do produto com desconto:R${}'.format(total))
elif opcao == 2:
     total = produto - produto * 0.05
     print('Valor do produto com desconto Cartao a vista:R${}'.format(total))
elif opcao == 3:
    total = produto
    print('Valor parcelado em ate 2X no Cartao:{}'.format(total))
elif opcao == 4:
    total = produto + produto * 0.20
    print('Valor do produto com Juros parcelados em 3x ou mais:R${}'.format(total))
else:
    print('Opcao invalida.')

