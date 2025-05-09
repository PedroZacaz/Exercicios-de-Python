print('--- LOJA ZACARIAS ---')
produto = float(input('Qual o preço do produto: '))
pagamento = str(input('Qual a forma de pagamento? Digite: \n '
                      '[ 1 ] Dinheiro/cheque \n [ 2 ] Cartão (vista ou parcelado) \n')).strip().lower()

#Pagamento com DINHEIRO/CHEQUE
#O metodo startswith() é usado para verificar se uma 'string' começa com um determinado texto
if pagamento.startswith(('dinheiro', 'cheque', 'dinheiro/cheque', 'cheque/dinheiro', '1')):
    print('Pagamento selecionado: DINHEIRO/CHEQUE \n'
          'Desconto de 10%')
    desconto = produto * 0.10
    valorFinal = produto - desconto
    print(f'O valor final com desconto será de R${valorFinal:.2f}')

#Pagamento com CARTÃO e à vista
elif pagamento.startswith(('cartão', 'vista', 'cartao', 'parcelado', '2')):
    forma_cartao = input('Pagamento selecionado: CARTÃO \n Qual forma: \n [ 1 ] À vista \n [ 2 ] Parcelado \n')
    if forma_cartao.startswith(('á vista', 'vista', 'a vista', '1')):
        print('Pagamento: Á VISTA')
        desconto = produto * 0.05
        valorFinal = produto - desconto
        print(f'Valor Final R${valorFinal:.2f}')


    # Pagamento com CARTÃO PARCELADO
    elif forma_cartao.startswith(('parcelado', 'cartao parcelado', 'parcela', 'cartão parcelado','2')):
        print('Pagamento: PARCELADO')
        parcela = input('As parcelas podem ser em: \n [ 1 ] 2X \n [ 2 ] 3x ou mais \n').lower()
        if parcela.startswith(( '2x', '1')):
            parcela2 = produto / 2
            print(f'Pagamento final será 2X, sem desconto. VALOR FINAL R${produto} e com parcelas de R${parcela2}')
            # Pagamento com Parcela com juros
        elif parcela.startswith(('3x', '2', 'mais')):
            parcelaMais = int(input('Quantas parcelas (juros de 20%)? \n'))
            juros = produto * 0.20
            valorFinal = produto + juros
            parcela3 = valorFinal / parcelaMais
            print(f'Valor final será R${valorFinal:.2f} , com parcelas de R${parcela3:.2f} em {parcelaMais}x')
