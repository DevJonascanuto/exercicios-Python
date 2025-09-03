'''faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo
retangulo, calcule e mostre o comprimento da hipotenusa'''

import math
print ('vou calcular o comprimento da hipotenusa, siga os proximos passos ')

cateto_oposto = float(input('digite o comprimento do cateto oposto '))
cateto_adjacente = float(input('digite o comprimento do cateto adjacente '))
hipotenusa = math.hypot (cateto_oposto,cateto_adjacente)


print (f'a hipotenusa de {cateto_oposto} e {cateto_adjacente} é {hipotenusa:.2f}')

