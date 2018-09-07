cd = ce = 0
ex = list(str(input('Digite a expressao: ')))
for c in range(len(ex)):
    if ex[c] == '(':
        ce += 1
    elif ex[c] == ')':
        cd += 1
if ce == cd:
    print('Expressao Valida..')
else:
    print('Expressao invalida..')