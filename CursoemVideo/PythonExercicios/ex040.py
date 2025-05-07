n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))
media = (n1+n2)/2

if media < 5:
    print(f'Sua média {media:.1f} está abaixo de 5: REPROVADO')
elif media >= 7:
    print(f'Sua média {media:.1f} está ótima, você está: APROVADO')
elif 7 > media >= 5:
    print(f'A média {media:.1f} está na zona de: RECUPERAÇÃO')

#era só usar a matemática
'''elif media <= 6.9:
    print(f'A média {media:.1f} está na zona de: RECUPERAÇÃO')'''
