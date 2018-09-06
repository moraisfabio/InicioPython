print('Tabuada')
print('-=-'*10)

while True:
    print('=' * 20)
    n = int(input('QUER VER A TABUADA DE QUAL VALOR?: '))
    print('=' * 20)
    tab = n * 1
    tab1 = n * 2
    tab2 = n * 3
    tab3 = n * 4
    tab4 = n * 5
    tab5 = n * 6
    tab6 = n * 7
    tab7 = n * 8
    tab8 = n * 9
    tab9 = n * 10
    if n < 0:
        break
    print(f'{n} x 1 = {tab} \n{n} x 2 = {tab1} \n{n} x 3 = {tab2} \n{n} x 4 = {tab3} \n{n} x 5 = {tab4}'
          f'\n{n} x 6 = {tab5} \n{n} x 7 = {tab6} \n{n} x 8 = {tab7} \n{n} x 9 = {tab8} \n{n} x 10 = {tab9}')

print('PROGRAMA TABUADA ENCERRADO, VOLTE SEMPRE!!')
