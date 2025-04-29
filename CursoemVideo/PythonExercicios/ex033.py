n1 = int(input('Digite o Primeiro número: '))
n2 = int(input('Digite o Segundo número: '))
n3 = int(input('Digite o Terceiro número: '))

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

print(f'Menor: {menor}')
print(f'Maior: {maior}')


''' Isso não utiliza Condição
junto= [n1,n2,n3]
maior = max(junto)
menor = min(junto)
'''