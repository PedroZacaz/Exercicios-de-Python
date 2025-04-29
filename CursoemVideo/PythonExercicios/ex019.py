"""import random

al1 = str(input('Digite o 1° nome do aluno: '))
al2 = str(input('Digite o 2° nome do aluno: '))
al3 = str(input('Digite o 3° nome do aluno: '))
al4 = str(input('Digite o 4° nome do aluno: '))

junto = (al1,al2,al3,al4) #Devia ter colocado entre [], não em (). O [] significa 'lista'.
sorteio = random.sample(junto, k=1)

print(f'O escolhido para limpar a lousa é: {sorteio}')"""

#Como é feito no video
from random import choice

al1 = str(input('Digite o 1° nome do aluno: '))
al2 = str(input('Digite o 2° nome do aluno: '))
al3 = str(input('Digite o 3° nome do aluno: '))
al4 = str(input('Digite o 4° nome do aluno: '))
lista = [al1, al2, al3, al4]
escolhido = choice(lista)

print(f'O escolhido para limpar a lousa é: {escolhido}')