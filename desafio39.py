ano = int(input('Informe o ano de seu nascimento:'))
alistar = 2018 - ano
if alistar < 18:
    falta = 18 - alistar
    print('Falta:{} ano para voce se alistar'.format(falta))
elif alistar == 18:
    falta = 18 - alistar
    print('Ja esta na hora de voce se alistar.')
elif alistar > 18:
    falta = alistar - 18
    print('O tempo ja estourou para o alistamento em:{} anos.'.format(falta))