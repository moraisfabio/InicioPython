s = 0
for c in range(0, 6):
    dig = int(input('Informe um valor:'))
    if dig % 2 == 0:
        s += dig
print(s)