lista = list ()
par = list()
impar = list()
for c in range(0, 7):
    lista.append(int(input('Informe um valor: ')))
for p in lista:
    if p % 2 == 0:
        par.append(p)
    else:
        impar.append(p)
print('-='*30)
print(f'Os valores pares sao {sorted(par)} em ordem crescente')
print(f'Os valores impares sao {sorted(impar)} em ordem crescente')


