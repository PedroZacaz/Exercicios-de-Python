from datetime import date

ano = int(input('Digite o ano para saber se é Bissexto: '))
# Analisa o ano atual da máquina
if ano == 0:
    ano = date.today().year
bis = ano % 4

# Para ser ano bissexto não pode ser divisível por 100
if bis == 0 and ano % 100 !=0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} não é BISSEXTO')