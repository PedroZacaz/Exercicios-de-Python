n1 = float(input('Digite a Primeira nota: '))
n2 = float(input('Digite a Segunda nota: '))
m = (n1+n2) / 2
print(f'Sua média foi {m:.1f}')

#Consição Simplificada
print('Sua média é BOA' if m >=6 else 'ESTUDE MAIS')
#Condição
"""
if m >= 6:
    print('Sua nota está muito boa! PARABÉNS')
else:
    print('Sua nota é horroroso! ESTUDE MAIS E APRENDA!')
"""