print('-_'*20)
print('Analisador de Triângulos')
print('-_'*20)
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if a + b > c and a + c > b and b + c > a:
    print('Essas retas forma um triângulo sim, pode confiar')
else:
    print('Não forma um triângulo, medidas incongruentes')