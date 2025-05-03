n1 = int(input('Digite o 1° Número: '))
n2 = int(input('Digite o 2° Número: '))
azul = '\33[34m'
verde = '\33[32m'
limpar = '\33[m'

if n1 < n2:
    print(f'O {verde}2° valor{limpar} que é{azul} {n2}{limpar}, é maior.')
elif n2 < n1:
    print(f'O {verde}1° valor{limpar} que é{azul} {n1}{limpar}, é maior>')
else:
    print(f'Os valores são iguais.')