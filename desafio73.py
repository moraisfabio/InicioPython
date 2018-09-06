tabela = ('Sao Paulo', 'Internacional', 'Flamengo', 'Palmeiras', 'Gremio', 'Atletico', 'Cruzeiro', 'Corinthians', 'America-MG', 'Fluminense', 'Bahia', 'Botafogo'
          'Atetico-PR',  'Santos', 'Vasco da Gama', 'EC Vitoria', 'Chapecoense', 'Sport Recife', 'Ceara SC', 'Parana')
print(f'Os 5 primeiros colocados {tabela[0:6]} \nOs Ultimos 5 colocados {tabela[14:]} \nA Classificacao em ordem alfabetica {sorted(tabela)}')
for pos, Chapecoense in enumerate(tabela):
    if pos == 15:
        print(f'A Chapecoense esta na {[pos]} posicao')

