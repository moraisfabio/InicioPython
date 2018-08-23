la1 = float(input('Informe o valor do lado 1:'))
la2 = float(input('Informe o valor do lado 2:'))
la3 = float(input('Informe o valor do lado 3:'))

if la1 == la2 and la3:
    print('Triangulo Equilatero.')
elif la1 == la2 != la3:
    print('Triangulo Isoceles.')
elif la1 != la2 != la3:
    print('Triangulo Escaleno.')
