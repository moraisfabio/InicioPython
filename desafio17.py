from math import hypot, sin , atan
co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjancente: '))
print('O valor da hipotenusa: {}'.format(hypot(co, ca)))
#print('A Hipotenusa vale: {} '.format(co/sin(atan(co/ca))))