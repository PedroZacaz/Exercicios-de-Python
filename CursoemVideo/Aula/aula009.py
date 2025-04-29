frase = 'Curso em Vídeo Python'
dividido = frase.split()

#print(frase[3])
#print(frase[3:13])
#print(frase[:13])
#print(frase[1:15])
#print(frase[1:15:2])
#print(frase[::2])


#print("""Olá, eu sou Pedro e estou aprendendo a linguagem python atraves do canal
#Curso em video, estou tendo uma otima experiencia, queria externar minha
#gratidão a todos que colaboraram para a existencia desse curso e sua
#disponibilidade gratuita no youtube.""")           #Quando colocar 3" (""") permite colocar textos grandes.

#print(frase.count('o'))
#print(frase.upper().count('O'))
#print(len(frase))                          #Quantidade de caracter
#print(len(frase.strip()))                  #Remove espaços desnecessario
#print(frase.replace('Python', 'Android'))  #Troca a palavra
#print('Curso' in frase)                    #Se existe a palavra
#print(frase.find('Vídeo'))                 #Encontra a posição da palavra, se não existe ele retorna -1
#print(frase.lower().find('vídeo'))

"""""Parte do Dividido"""""
#print(dividido)
#print(dividido[0])             #Pega o primeiro da lista
print(dividido[2][3])
print('-'.join(frase))          #Retorna: C-u-r-s-o- e-m -V-í-d-e-o
print('-'.join(frase.split()))  #Retorna: Curso-em-Vídeo