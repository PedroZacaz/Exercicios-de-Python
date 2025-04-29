n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

#print('Soma: {}\n Produto: {}\n Divisão:{:0.3}\n'.format(s,m,d), end=' ')
#print('Divisão Inteira: {}\n Potência: {}'.format(di,e))

print('Soma: {}, Produto: {}, Divisão: {:0.3},'.format(s,m,d), end=' ')
print('Divisão Inteira: {}, Potência: {}.'.format(di,e))

#print('Soma: {}\n Produto: {}\n Divisão:{:0.3}\n'.format(s,m,d), end=' === ')
#print('Divisão Inteira: {}\n Potência: {}'.format(di,e))

#Todos funcionam.
#O "end" serve para que o codigo continue na mesma linha.