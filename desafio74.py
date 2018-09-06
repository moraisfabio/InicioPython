import random
maior = menor = 0
for c in range(0, 5):
    aleatorio = random.randint(1, 5)
    aleatorio1 = random.randint(6, 10)
    aleatorio2 = random.randint(11, 15)
    aleatorio3 = random.randint(16, 20)
    aleatorio4 = random.randint(21, 25)
tup = (aleatorio, aleatorio1 , aleatorio2, aleatorio3, aleatorio4)
print(tup)
for maior in tup:
    if aleatorio > maior:
        maior = aleatorio
for menor in tup:
    if aleatorio < menor:
        menor = aleatorio
print(f'O maior numero e:{maior} e o menor e:{menor}')
