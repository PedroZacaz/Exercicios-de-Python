#Biblioteca de cor ANSI
cor = {'vermelho': '\33[31m',
       'verde': '\33[32m',
       'anil': '\33[34m',
       'azul': '\33[36m',
       'amarelo': '\33[33m',
       'limpar': '\33[m'}

n1 = int(input(f'Digite o {cor['verde']}Primeiro número:{cor['limpar']} '))
n2 = int(input(f'Digite o {cor['amarelo']}Segundo número:{cor['limpar']} '))
n3 = int(input(f'Digite o {cor['anil']}Terceiro número:{cor['limpar']} '))

# Verificar se é menor
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
# Verificar se é maior
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print(f'{cor['vermelho']}Menor: {menor}{cor['limpar']}')
print(f'{cor['azul']}Maior: {maior}{cor['limpar']}')


''' Isso não utiliza Condição
junto= [n1,n2,n3]
maior = max(junto)
menor = min(junto)
'''