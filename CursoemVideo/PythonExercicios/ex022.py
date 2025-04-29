nome = str(input('Digite o seu nome completo: ')).strip() #O ".strip" serve para tirar os espaços que vem antes e depois.
#Outro jeito para o len
#letras = len(nome) - nome.count('')
#Dizem nos cometários que é melhor criar uma variavel para fazer isso
print('Analisando o seu nome...')
print(f'Seu nome em maiúscula é {nome.upper()}.')
print(f'Seu nome em minúsculo é {nome.lower()}.')
print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} de letras.')
#print(f'Seu primeiro nome tem {nome.find(' ')} letras.')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras.')