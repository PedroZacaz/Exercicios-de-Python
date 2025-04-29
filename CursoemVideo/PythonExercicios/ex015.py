dia = int(input('Quantos dias ficou com o carro? '))
km = float(input('Quantos Km rodou com o carro? '))

pago = (dia*60)+(km*0.15)

print(f'O preço final do aluguel ficará: R${pago:.2f}')