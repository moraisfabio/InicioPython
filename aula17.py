'''num = [3, 2, 1, 5, 7]
num[2] = 6
num.append(8)
num.sort(reverse=True)
num.insert(3, 5)
num.pop(6)
num.remove(5)
print(num)
print(f'Essa lista tem {len(num)} elementos')'''
valores = list()
'''valores.append(8)
valores.append(5)
valores.append(9)'''
'''for cont in range(0, 5):
    valores.append(int(input('Digite um valor:')))

for c, v in enumerate(valores):
    print(f'na posicao {c} encontrei o valor {v}!')
print('Cheguei ao final da Lista')'''
a = [2, 3, 4]
b = a[:]
b[2] = 9
print(f'A lista A:{a}')
print(f'A lista B:{b}')