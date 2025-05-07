print('-='*15)
print('EMPRÉSTIMO PARA SUA CASA')
print('-='*15)

print('Entenda se será possível fazer um empréstimo para comprar a sua casa')
casa = float(input('Qual o valor da CASA: '))
sal = float(input('Quanto de salário você recebe: '))
ano = int(input('Em quantos anos pretende pagar a casa: '))

prestacao = casa / (ano * 12)
minimo = sal * 30 / 100

print(f'Para pagar uma casa de R${casa:.2f} em {ano} anos a prestação será de R$ {prestacao:.2f}')

if prestacao <= minimo:
    print(f'Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')