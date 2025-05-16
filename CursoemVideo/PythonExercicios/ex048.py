s = 0 # Acomulador
cont = 0 # Contador
for c in range(1, 501, 2):
    if c % 3 == 0:
        s =+ c # Acomulador
        cont = cont + 1 # Contador
print(f'A soma dos números {cont} resultara em: {s}')