real = float(input('Digite quanto dinheiro você brasileiro possui para converter: '))

dolar = float(real/3.27)
#hoje em dia (27/02/2025) // dolar = float(real/5.81)
# do video 3.27

print(f'O valor R${real:.2f} convertido para dolar é: ${dolar:.2f}')
