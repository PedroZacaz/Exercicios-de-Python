from random import randint

#cor
verde = '\33[32m'
azul = '\33[34m'
vermelho = '\33[31m'
amarelo = '\33[33m'
roxo = '\33[35m'
limpar = '\33[m'

print(f'{roxo}')
print('-'*18)
print(f'Jogo do JoKenPô!')
print('-'*18)
print(f'{limpar}')

jogadorMao = int(input(f'Qual mão você quer jogar: {azul}\n 1[Pedra] \n 2[Papel] \n 3[Tesoura] \n {limpar}Digite: '))
compMao = randint(1,3)

#PEDRA
if jogadorMao == 1 and compMao == 1:
    print(f'{amarelo}EMPATE{limpar} - Os dois colocaram {amarelo}PEDRA x PEDRA{limpar}')
elif jogadorMao == 1 and compMao == 2:
    print(f'{vermelho}DERROTA{limpar} - Computador venceu com {vermelho}PAPEL x PEDRA{limpar}')
elif jogadorMao == 1 and compMao == 3:
    print(f'{verde}VITÓRIA{limpar} - Você venceu com {verde}PEDRA x TESOURA{limpar}')

#PAPEL
elif jogadorMao == 2 and compMao == 1:
    print(f'{verde}VITÓRIA{limpar} - Você venceu com {verde}PAPEL x PEDRA{limpar}')
elif jogadorMao == 2 and compMao == 2:
    print(f'{amarelo}EMPATE{limpar} - Os dois colocaram {amarelo}PAPEL x PAPEL{limpar}')
elif jogadorMao == 2 and compMao == 3:
    print(f'{vermelho}DERROTA{limpar} - Computador venceu com {vermelho}TESOURA x PAPEL{limpar}')

#TESOURA
elif jogadorMao == 3 and compMao == 1:
    print(f'{vermelho}DERROTA{limpar} - Computador venceu com {vermelho}PEDRA x TESOURA{limpar}')
elif jogadorMao == 3 and compMao == 2:
    print(f'{verde}VITÓRIA{limpar} - Você venceu com {verde}TESOURA x PAPEL{limpar}')
elif jogadorMao == 3 and compMao == 3:
    print(f'{amarelo}EMPATE{limpar} - Os dois colocaram {amarelo}TESOURA x TESOURA{limpar}')

else:
    print(f'{vermelho}ERRO - VALOR INVÁLIDO{limpar}')