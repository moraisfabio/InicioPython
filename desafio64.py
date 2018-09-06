print('Desafio Flag 999')
print('-=-'*20)
n = sm = cont = 0
n = int(input('Digite um numero:'))
while n != 999:
   sm += n
   cont += 1
   n = int(input('Digite um numero:'))
print('Total de numeros digitados: {} e soma: {}'.format(cont, sm))