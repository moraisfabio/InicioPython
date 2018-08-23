frase = str(input('Digite uma Frase:').replace('', '').lower())
if frase == frase[::-1]:
    print('Palidromo.')
else:
    print('Nao e um palidromo.')