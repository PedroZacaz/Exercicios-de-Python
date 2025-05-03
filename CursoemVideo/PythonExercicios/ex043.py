peso = int(input('Diga quanto que você pesa: '))
altura = float(input('Diga qual é a sua altura: '))
imc = peso / altura**2

if imc < 18.5:
    print(f'O seu IMC {imc:.2f} mostra que você está: ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print(f'O seu IMC {imc:.2f} mostra que você está: PESO IDEAL')
elif 25 <= imc < 30:
    print(f'O seu IMC {imc:.2f} mostra que você está: SOBREPESO')
elif 30 <= imc < 40:
    print(f'O seu IMC {imc:.2f} mostra que você está: OBESIDADE')
else:
    print(f'Você está: OBESIDADE MÓRBIDA')