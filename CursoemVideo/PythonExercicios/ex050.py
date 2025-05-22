soma = 0 # Acomulador
cont = 0 # Contador
for i in range(1,7):
    num = int(input(f'Digite o {i} número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Informou {cont} de números PARES e a soma foi {soma}')
