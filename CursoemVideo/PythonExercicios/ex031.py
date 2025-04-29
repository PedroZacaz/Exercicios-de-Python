dist = float(input('Qual a distância da viagem em Km: '))

# If else simplificado
#preco = dist * 0.50 if dist<= 200 else dist * 0.45

if dist > 200:
    long = dist * 0.45
    print(f'O valor da passagem é R${long}')
else:
    small = dist * 0.50
    print(f'O valor da passagem é R${small:.2f}')
#print(f'O preço da passagem será de R${preco:.2f}')