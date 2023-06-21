n1 = int(input('um numero; '))
n2 = int(input('outro numero; '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
su = n1-n2
p = n1**n2
r = n1%n2
print('A soma é {}, a subtrção é {}, o produto é {}, e a divisão é {:.3f}'.format (s, su, m, d), end='')
print('A divisão inteira é {}, a potencia é {}'.format (di, p), end='')
print('E o resto da divisão é {}'.format (r))