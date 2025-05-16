'''i = int(input('início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')'''

s = 0

for c in range (0, 4):
    n = int(input('Digite um valor: '))
    #Jeito python
    s += n
    #Jeito normal
    #s = s + n ''Muito normal''
print(f'O somatório de tudo é: {s}')