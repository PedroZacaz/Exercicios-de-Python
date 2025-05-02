print('\33[7;30;47m Olá Mundo!\33[m')

nome = 'Zacarias'
#Isso é uma Biblioteca com códigos de escape sequence ANSI para configurar cores
cor = {'limpar': '\033[m',
       'azul': '\033[34m',
       'amarelo': '\033[33m',
       'pretoBranco': '\033[7;30m'}

print(f'O seu nome é {cor['azul']}{nome}{cor['limpar']}')