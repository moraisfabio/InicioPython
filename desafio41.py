ano = int(input('Informe o ano de nascimento:'))
cat = 2018 - ano
if cat <= 9:
    print('Ate 9 anos:Categoria Mirim')
elif cat > 9 and cat <= 14:
    print('Ate 14 anos:Categoria Infantil.')
elif cat > 14 and cat <= 19:
    print('Ate 19 anos:Categoria Junior.')
elif cat > 19 and cat <= 20:
    print('Ate 20 anos:Categoria Senior.')
else:
    print('Categoria Master')