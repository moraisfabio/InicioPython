valor = float(input('Qual o valor da Casa: '))
salario = float(input('Qual o seu salario: '))
periodo = float(input('Total de anos para pagar:'))

periodo = periodo * 12
prestacao = valor / periodo
per = salario - salario * 0.30
if prestacao > per:
    print('Infelizento nao podemos fazer o emprestimo.')
else:
    print('Emprestimo realizado com sucesso.')
