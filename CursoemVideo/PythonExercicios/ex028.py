from random import choice
from time import sleep # Faz o programa esperar por um tempo
print('JOGO DA ADIVINHAÇÃO')
print('=_=' *20)
nun_user = int(input('Digite um número para que o computador adivinhe: '))
print('PROCESSANDO...')
sleep(2)
    # random.choice(seq) → Escolhe um item aleatório de uma sequência
    # Exemplo: random.choice([1, 2, 3, 4, 5]) → Retorna um número entre 1 e 5
nun_comp = choice(range(6))
    # range(5) → Gera 0, 1, 2, 3, 4
    # range(1, 6) → Gera 1, 2, 3, 4, 5
    # range(1, 10, 2) → Gera 1, 3, 5, 7, 9
if nun_comp == nun_user:
    print('Parabéns! Você acertou :)')
else:
    print(f'Vish, acertou não. O número que pensei foi {nun_comp}. Tente novamente...')
print('=_=' * 20)