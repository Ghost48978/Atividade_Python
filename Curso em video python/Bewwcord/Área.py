#Meu codigo

A = float(input())
B = float(input())
C = float(input())
triangulo = A*C/2
círculo = 3.14159*C**2
trapezio = (A+B)*C/2
quadrado = B**2
retângulo = A*B
print ("TRIANGULO: {:.3f}".format(triangulo))
print ("CIRCULO: {:.3f}".format(círculo))
print ("TRAPEZIO: {:.3f}".format(trapezio))
print ("QUADRADO: {:.3f}".format(quadrado))
print ("RETANGULO: {:.3f}".format(retângulo))

#"Jeito certo"

valor = input().split(" ")

a, b, c = valor
pi = 3.14159

triangulo = (float(a) * float(c))/2
circulo = pi * (float(c)* float(c))
trapezio = float(c) *(float(a) + float(b)) / 2
quadrado = float(b) * float(b)
retangulo = float(a) * float(b)


print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f" % (triangulo, circulo, trapezio, quadrado, retangulo))