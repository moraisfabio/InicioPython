'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''
'''galera = [['Joao', 20], ['Fabio', 25], ['Ligia', 36], ['Gringas', 20]]
print(galera[2][0])
for p in galera:
    print(p[0])'''
galera = list()
dado= list()
for c in range(0, 2):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)