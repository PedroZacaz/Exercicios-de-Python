print('-='*15)
print('EMPRÉSTIMO PARA SUA CASA')
print('-='*15)

print('Entenda se será possível fazer um empréstimo para comprar a sua casa')
casa = float(input('Qual o valor da CASA: '))
sal = float(input('Quanto de salário você recebe: '))
ano = float(input('Em quantos anos pretende pagar a casa: '))

prestacao = casa / ano
mensal = (prestacao / 12)
calc = mensal - mensal * 0.30

print(f'O valor da prestação é {prestacao:.2f}')

if calc > sal:
    print(f'Você não vai poder fazer o emprétimo, o seu salário não permite.')
elif calc < sal:
    print(f'Você pode fazer o empréstimo, o valor será por ano R$ {prestacao:.2f} e a mensalidade é R$ {mensal:.2f}')
