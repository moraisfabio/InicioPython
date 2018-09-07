n = 0
while n < 10:
     p = int(input('Informe um numero:'))
     n += 1
     if p == 8:
        print('Voce acertou, mais precisou de {} vezes'.format(n))
        break
print('FIM')