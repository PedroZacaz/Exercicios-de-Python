from datetime import date
ano = int(input('Digite seu ano para saber a classificação: '))
idade = date.today().year - ano

if idade <= 9:
    print(f'Sua idade de {idade} está na categoria: MIRIM')
elif idade <= 14:
    print(f'Sua idade de {idade} está na categoria: INFANTIL')
elif idade <= 19:
    print(f'Sua idade de {idade} está classificado: JUNIOR')
elif idade <= 20:
    print(f'Sua idade de {idade} está na categoria: SÊNIOR')
elif idade > 20:
    print(f'Sua idade de {idade} está na categoria: MASTER')