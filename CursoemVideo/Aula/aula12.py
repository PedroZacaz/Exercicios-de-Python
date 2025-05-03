nome = str(input('Qual o seu nome? '))
if nome == 'José':
    print('Seu nome é bem Bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('O seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana Fernanda':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um Bom dia, {nome}!')