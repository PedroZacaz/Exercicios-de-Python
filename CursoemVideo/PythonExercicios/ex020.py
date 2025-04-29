"""import random

al1 = str(input('Digite o 1° nome do aluno: '))
al2 = str(input('Digite o 2° nome do aluno: '))
al3 = str(input('Digite o 3° nome do aluno: '))
al4 = str(input('Digite o 4° nome do aluno: '))

junto = [al1,al2,al3,al4]
sorteio = random.sample(junto, k=4)

print(f'Os escolhidos para apresentar é: {sorteio}')
#print(f'Os escolhidos para apresentar é: 1°{sorteio}, 2°{sorteio}, 3°{sorteio}, 4°{sorteio}')"""

#Como é feito no video
import random

al1 = input('1° Aluno: ')
al2 = input('2° Aluno: ')
al3 = input('3° Aluno: ')
al4 = input('4° Aluno: ')
junto = [al1, al2, al3, al4]
random.shuffle(junto)

print(f'A ondem de apresentação: \n {junto}')