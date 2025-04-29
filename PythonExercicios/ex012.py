produto = float(input('Qual o valor do produto? '))

desc = float(produto - (produto * 0.05))

print(f'O preço do produto R${produto:.2f} com desconto é R${desc:.2f}!')