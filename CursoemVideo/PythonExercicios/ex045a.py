#Codigo feito no vídeo
from random import randint
from time import sleep

#Biblioteca
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print(f'Jogo do JoKenPô!')
print('''Suas opções:
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')
jogadorMao = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print(f'Computador jogou {itens[comp]}')
print(f'Jogador jogou {itens[jogadorMao]}')
print('-=' * 11)

if comp == 0: # Computador jogou PEDRA
    if jogadorMao == 0:
        print('EMPATE')
    elif jogadorMao == 1:
        print('JOGADOR VENCE')
    elif jogadorMao == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif comp == 1: # Computador jogou PAPEL
    if jogadorMao == 0:
        print('COMPUTADOR VENCE')
    elif jogadorMao == 1:
        print('EMPATE')
    elif jogadorMao == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif comp == 2: # Computador jogou TESOURA
    if jogadorMao == 0:
        print('JOGADOR VENCE')
    elif jogadorMao == 1:
        print('COMPUTADOR VENCE')
    elif jogadorMao == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')