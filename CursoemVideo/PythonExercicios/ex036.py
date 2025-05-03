print('-='*15)
print('EMPRÉSTIMO PARA SUA CASA')
print('-='*15)

print('Entenda se será possível fazer um empréstimo para comprar a sua casa')
casa = float(input('Qual o valor da CASA: '))
sal = float(input('Quanto de salário você recebe: '))
ano = int(input('Em quantos anos pretende pagar a casa: '))

prestacao = casa / ano

print(f'O valor da prestação é {prestacao}')

if prestacao < sal:
    print('i')

#incompleto