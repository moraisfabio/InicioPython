lista = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]').lower())
    if resp in 'n':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*25)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
while True:
    print('-'*35)
    opc = int(input('Deseja mostrar a nota de qual aluno? (999 Interrompe)'))
    if opc == 999:
        break
    if opc <= len(lista) -1:
        print(f'Notas de {lista[opc][0]} sao {lista[opc][1]}')
print('Finalizado.')