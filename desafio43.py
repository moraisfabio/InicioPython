peso = float(input('Informe seu peso:'))
altura = float(input('Informe a sua altura:'))
alt = altura * altura
imc = peso / alt
if imc < 18.5:
    print('abaixo do Peso.')
elif imc >= 18.5 and imc <= 25:
    print('Peso Ideal.')
elif imc >= 25 and imc <= 30:
    print('Sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Obesidade.')
elif imc > 40:
    print('Obesidade Morbida.')
