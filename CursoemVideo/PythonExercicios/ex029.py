vel = int(input('Digite a velocidade do carro: '))
if vel > 80:
    print('Passou do limite de velocidade, você será multado')
    multa = (vel - 80) * 7
    print(f'O valor da multa é R$ {multa},00')
#     Não tem a necessidade de ter 'else', quando isso acontece é chamado de Condição simples
# else:
#     print('Dentro do limite de velocidade')
print('Siga as leis de trânsito')