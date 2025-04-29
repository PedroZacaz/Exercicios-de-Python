'''from my_matth1 import My_mat

num1 = My_mat.seno(int(input('Digite o valor de seno')))

print(f'O valor do seno é {num1}')
#incompleto'''

import math

angulo = float(input('Digite o valor do ângulo:'))
sin = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(f'O valor de seno {sin:.2f}')
print(f'O valor do cosseno {cos:.2f}')
print(f'O valor da tangente {tan:.2f}')
