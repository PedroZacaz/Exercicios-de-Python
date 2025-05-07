produto = float(input('Qual o preço do produto: '))
pagamento = str(input('Qual a forma de pagamento? Digite: dinheiro/cheque ou cartão (vista ou parcelado) \n')).strip().lower()

#O metodo startswith() é usado para verificar se uma 'string' começa com um determinado texto
if pagamento.startswith(('dinheiro', 'cheque', 'dinheiro/cheque', 'cheque/dinheiro')):
    print('Pagamento selecionado: DINHEIRO/CHEQUE \n'
          'Desconto de 10%')
    desconto = produto * 0.10
    valorFinal = produto - desconto
    print(f'O valor final com desconto será de R$ {valorFinal:.2f}')

elif pagamento.startswith(('cartão', 'vista', 'cartao', 'parcelado')):
    forma_cartao = input('Pagamento selecionado: CARTÃO \n Qual forma: á vista ou parcelado: ')
    if forma_cartao.startswith(('á vista', 'vista', 'a vista')):
        print('Pagamento: Á VISTA')
        desconto = produto * 0.05
        valorFinal = produto - desconto
        print(f'Valor Final R$ {valorFinal:.2f}')

    if forma_cartao.startswith(('parcelado', 'cartao parcelado', 'parcela', 'cartão parcelado')):
        print('Pagamento: PARCELADO')
        parcela = input('As parcelas podem ser em 2X ou 3x, qual será? ')
        if parcela.startswith(('2X', '2x', '2')):
            parcela2 = produto / 2
            print(f'Pagamento final será 2X, sem desconto. VALOR FINAL R$ {produto} e com parcelas de R$ {parcela2}')
        elif parcela.startswith(('3X', '3x', '3')):
            print(f'Pagamento final será 3X, com juros de 20%')
            juros = produto * 0.20
            valorFinal = produto + juros
            parcela3 = valorFinal / 3
            print(f'Valor final será R$ {valorFinal:.2f} , com parcelas de R$ {parcela3}')
