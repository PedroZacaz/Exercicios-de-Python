#Biblioteca de cor ANSI
cor = {'vermelho': '\33[31m',
       'verde': '\33[32m',
       'amarelo': '\33[33m',
       'azul': '\33[34m',
       'limpar': '\33[m'}

sal = float(input(f'Qual o seu {cor['amarelo']}salário: {cor['limpar']}'))
print(f'{cor['azul']}Parabéns!{cor['limpar']} Você recebeu um {cor['verde']}aumento{cor['limpar']}.')

if sal <= 1250.00:
    menor = ((sal * 15) / 100) + sal
    print(f'O seu {cor['amarelo']}salário de R${sal}{cor['limpar']} agora será de {cor['azul']}R${menor}{cor['limpar']}')
else:
    maior = ((sal * 10) / 100) + sal
    print(f'O seu {cor['amarelo']}salário de R${sal}{cor['limpar']} agora será {cor['verde']}R${maior}{cor['limpar']}')