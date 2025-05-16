from time import sleep
import  pygame
import emoji

print('--- CONTAGEM REGRESSIVA ---')
for c in range(10, -1, -1):
    sleep(1) #é só isso?
    print(c)

#emoji de confete
print(emoji.emojize('É FESTA!!!! 🎉 🎊 🎉 🎊 🎉'))
#Som de Fogo de artificio
pygame.init()
pygame.mixer.music.load('ex046-fogo-de-artificio.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()