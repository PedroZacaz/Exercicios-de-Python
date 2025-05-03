from datetime import date

ano = int(input('Qual o ano que você nasceu: '))
idade = date.today().year - ano
#cor
verde = '\33[32m'
azul = '\33[34m'
limpar = '\33[m'

#Descobrir se vai se alistar
if idade < 18:
    tempo_falta = 18 - idade
    print(f'Você ainda {verde}não vai se alistar esse ano{limpar}. Você está com {azul}{idade}{limpar}.')
    print(f'Falta {tempo_falta} ano(s) para completar 18 anos.')
elif idade == 18:
    print(f'Você vai completar {verde}18 esse ano{limpar}. {azul}Está na hora de se alistar{limpar}.')
else:
    tempo_falta = idade - 18
    print(f'Já se passou do tempo do alistamento,{azul} toma cuidado{limpar}.')
    print(f'Se passaram {abs(tempo_falta)} ano(s) em que você deveria ter se apresentado.')