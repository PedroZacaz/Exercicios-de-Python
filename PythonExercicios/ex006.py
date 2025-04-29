n1 = int(input('Digite o númerico: '))
d = n1*2
t = n1*3
raiz = n1**(1/2)

#print('O resultado do {}, são as seguintes: \n Dobro: {} \n Triplo: {} \n Raiz: {:0.3}'.format(n1,d,t,raiz))
#print('O resultado do {}, são as seguintes: \n Dobro: {} \n Triplo: {} \n Raiz: {:0.3}'.format(n1,(n1*2),(n1*3),(n1**(1/2))))
print(f'O resultado do {n1}, são as seguintes: \n Dobro: {n1*2} \n Triplo: {n1*3} \n Raiz: {(n1**(1/2)):0.2f}')
#esse é o mais atual, eu acho...                       nessa parte pode fazer assim também {pow(n1,(1/2)):0.2f} "vai dar a mesma coisa"