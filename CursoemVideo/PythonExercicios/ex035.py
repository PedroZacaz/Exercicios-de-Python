#Biblioteca de cor ANSI
cor = {'vermelho': '\33[31m',
       'verde': '\33[32m',
       'azul': '\33[34m',
       'amarelo': '\33[33m',
       'roxo': '\33[35m',
       'limpar': '\33[m'}

print(f'{cor['amarelo']}-_{cor['amarelo']}'*20)
print('Analisador de Triângulos')
print(f'{cor['amarelo']}-_{cor['amarelo']}'*20)
a = float(input(f'{cor['roxo']}Digite o primeiro número:{cor['limpar']} '))
b = float(input(f'{cor['amarelo']}Digite o segundo número:{cor['limpar']} '))
c = float(input(f'{cor['azul']}Digite o terceiro número:{cor['limpar']} '))

if a + b > c and a + c > b and b + c > a:
    print(f'{cor['verde']}Essas retas forma um triângulo sim, pode confiar{cor['limpar']}')
else:
    print(f'{cor['vermelho']}Não forma um triângulo, medidas incongruentes{cor['limpar']}')