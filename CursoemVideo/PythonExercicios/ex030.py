print('Digite o número para saber se é PAR ou ÍMPAR')
num = int(input('Escreva: '))
calculo = num % 2

if calculo == 0:
    print('O número é PAR')
else:
    print('O número é ÍMPAR')