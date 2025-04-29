sal = float(input('Qual o seu salário: '))
print('Parabéns! Você recebeu um aumento.')

if sal <= 1250.00:
    menor = ((sal * 15) / 100) + sal
    print(f'O seu salário de R${sal} agora será de R${menor}')
else:
    maior = ((sal * 10) / 100) + sal
    print(f'O seu salário de R${sal} agora será R${maior}')