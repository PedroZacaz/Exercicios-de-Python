'''from math import sqrt, pow
#não foi muito necessario esse import, dava pra fazer usando **(1/2)
co = int(input('Didite o valor do Cateto Oposto: '))
ca = int(input('Digite o valor do Cateto Adjacente: '))
h = sqrt(pow(co,2)+pow(ca,2))

print(f'Com os valores do CO {co} e CA {ca}, pode se determinar que o \n '
      f'valor da hipotenusa é: {h:.2f}')'''

#O mais "fácil" ou a importação "correta"
import math

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto ajacente: '))
hi = math.hypot(co,ca)

print(f'O valor da hipotenusa é: {hi:.2f}')