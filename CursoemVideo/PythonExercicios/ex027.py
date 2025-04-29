nome = str(input('Digite o seu nome completo: ')).strip()
n = nome.split()
print(f'O seu primeiro nome é {n[0]}')
print(f'Seu último nome é {n[-1]}')

#print('Seu último nome é {}'.format(n[len(n)-1]))
#print(f'Seu último nome é {n[-1]}')
