print('Meu resultado')
n1 = float(input('Preço '))
d = n1*5/100
c = d-n1
print('O produto custa {} mais como hoje estamos com promoção ele saira apenas por {:.2f}'.format (n1, c))

print('Resultado do professor')
preço = float(input('Qual o valor do produto? R$'))
novo = preço - (preço*5/100)
print('O produto custava R${}, na promoção com desconto de 5% vai custar R${}'.format (preço, novo))