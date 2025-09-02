'''crie um programa que leia um numero real qualquer pelo teclado e mostre sua porção inteira 
ex: digite um numero : 6127
o numero 6127 tem a parte inteira 6.'''

import math

numero_real = float(input(' digite um numero real, que vou mostrar sua parte inteira '))
parte_inteira = math.trunc(numero_real)
print (f' a parte inteira de {numero_real} é {parte_inteira}')

