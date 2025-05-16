from time import sleep

par = 0
print('\033[0;31;40m CONTAGEM DOS NÚMEROS PARES ATÉ 50 \033[0m')
for c in range(1, 50+1):
    par = c % 2
    if par == 0:
        sleep(0.3)
        print(c)