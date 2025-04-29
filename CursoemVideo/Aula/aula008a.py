import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print(f'A raiz de {num} resultara em {raiz:.2f}')
#print(f'A raiz de {num} resultara em {math.floor(raiz)}.') "Redonda para baixo"
#                                     {math.ceil(raiz)} "Redonda para cima"

#importando somente o sqrt
from math import sqrt

num = int(input('Novamente, digite um número: '))
raiz = sqrt(num)

print(f'A raiz de {num} resultara em {raiz:.2f}')