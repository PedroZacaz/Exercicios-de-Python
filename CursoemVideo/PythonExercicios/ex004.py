coisa = input('Digite qualquer coisa(qualquer coisa mesmo): ')

print('O tipo primitivo é:',type(coisa))

print('Possui somente espaço?', coisa.isspace())
print('É um número?',coisa.isnumeric())
print('É alfabetica?',coisa.isalpha())
print('É alfanúmerico?',coisa.isalnum())
print('É maiúsculas?',coisa.isupper())
print('É minúscula?', coisa.islower())
print('É capitalizada?☭', coisa.istitle())


