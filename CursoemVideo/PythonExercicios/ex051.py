'''pt = int(input('Primeiro Termo: '))
rz = int(input('Razão: '))
for c in range(1, 11):
    pa = pt + (c - 1) * rz
    print(f'{pa} → ', end='')
print('FIM!')'''

# No video
pt = int(input('Primeiro Termo: '))
rz = int(input('Razão: '))
pa = pt + (10 - 1) * rz
for c in range(pt, pa + rz, rz):
    print(f'{c} ', end='→ ')
print('Acabou')