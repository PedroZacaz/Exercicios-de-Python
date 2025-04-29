n1 = int(input('Digite um número: '))
menor = n1-1
maior = n1+1
print('Analisando o número {} o resultado é:\n Antecessor: {}\n Sucessor: {}'.format(n1,menor,maior))

print(f'Analisando o número {n1} o resultado é:\n Antecessor: {(n1-1)}\n Sucessor: {(n1+1)}')
#No python 3.9.4, não é mais necessário usar o ".formart()" há uma maneira mais fácil.
#Trocar o ".format()" e usar o "f" antes das aspas.


print('Analisando o número {} o resultado é:\n Antecessor: {}\n Sucessor: {}'.format(n1,(n1-1),(n1+1)))
#Outra forma
#print('Analisando o número {} o resultado é:\n Antecessor: {}\n Sucessor: {}'.format(n1,(n1-1),(n1+1)))
#desse jeito não precisa declarar variavel, mas só se não precisar utiliza esses valores