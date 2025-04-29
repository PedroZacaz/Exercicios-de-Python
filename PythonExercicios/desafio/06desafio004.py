n=(input('Digite qualquer coisa: '))

print('Ele é alfanuméricos?',n.isalnum())
print('É uma letra?',n.isalpha())
print('É um decimal?',n.isdecimal())
print('É um numero?',n.isnumeric())
print('É uma caixa alta?',n.isupper())
print('Tem espaço?',n.isspace())
print('Ele é do Alfabeto?',n.isascii())

print(type(n))
