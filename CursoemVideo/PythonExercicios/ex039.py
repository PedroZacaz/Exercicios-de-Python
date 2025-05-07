from datetime import date

ano = int(input('Qual o ano que você nasceu: '))
idade = date.today().year - ano
atual = date.today().year
#cor
verde = '\33[32m'
azul = '\33[34m'
limpar = '\33[m'

#Descobrir se vai se alistar
if idade < 18:
    tempo_falta = 18 - idade
    alis = atual + tempo_falta
    print(f'Você ainda {verde}não vai se alistar esse ano{limpar}. Você está com {azul}{idade}{limpar}.')
    print(f'Falta {tempo_falta} ano(s) para completar 18 anos. O ano será {alis}')
elif idade == 18:
    print(f'Você vai completar {verde}18 esse ano{limpar}. {azul}Está na hora de se alistar{limpar}.')
else:
    tempo_falta = idade - 18
    alis = atual - tempo_falta
    print(f'Já se passou do tempo do alistamento,{azul} seu alistamento foi em {alis}{limpar}.')
    print(f'Se passaram {abs(tempo_falta)} ano(s) em que você deveria ter se apresentado.')