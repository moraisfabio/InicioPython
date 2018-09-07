lista = list()
par = list()
impar = list()
opcao = 0
while opcao != 'n':
   lista.append(int(input('Informe um valor: ')))
   opcao = str(input('Quer continuar?[S/N]:'))
print('-='*30)
print(f'A lista completa {lista}')
for n in lista:
    if n % 2 == 0:
       par.append(n)
    else:
        impar.append(n)

print(f'A lista de pares sao: {par}')
print(f'A lista de Impares sao:{impar}')


