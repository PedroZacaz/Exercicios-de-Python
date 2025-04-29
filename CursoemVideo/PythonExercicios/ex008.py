m = float(input('Digite o valor do metro: '))

mm = m*1000
cm = m*100
dm = m*10
#m = m*1
dam = m/10
hm = m/100
km = m/1000

print(f'O valor do Metro(s) {m}m será: \n Milímetros: {mm:.0f}mm \n Centímetros: {cm:.0f}cm \n Decímetro: {dm:.0f}dm')
print(f'Metro: {m:}m \n Decâmetro: {dam:}dam \n Hectômetro: {hm:}hm \n Quilômetro: {km:}km')

#print(f'Metro: {m:.0f}m \n Decâmetro: {dam:.2f}dam \n Hectômetro: {hm:.2f}hm \n Quilômetro: {km:.2f}km')