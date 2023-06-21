print('Meu jeito')

n1 = float(input('Qual seu salario? '))
r = 0.15*n1
c = r+n1
print('Seu salario de {} teve um aumento de {}, por conta do seu aumento agora seu salario passa a ser de {:.2f}.'.format (n1, r, c))

print('Jeito do professor')

salario = float(input('Qual o seu salariio? R$'))
novo = salario + (salario * 15 / 100)
print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format (salario, novo))