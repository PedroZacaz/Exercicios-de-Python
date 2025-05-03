from statistics import median

n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))
media = (n1+n2)/2

if media < 5:
    print(f'Sua média {media} está abaixo de 5: REPROVADO')
elif media >= 7:
    print(f'Sua média {media} está ótima, você está: APROVADO')
elif media >= 5:
    print(f'A média {media} está na zona de: RECUPERAÇÃO')
elif media <= 6.9:
    print(f'A média {media} está na zona de: RECUPERAÇÃO')
