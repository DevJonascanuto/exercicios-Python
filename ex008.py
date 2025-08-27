#escreva um programa que leia um numero inteiro qualkquer e mostre na tela sua taboada
numero = int(input('digite um numero inteiro, vou te mostrar a tabuada dele'))
print (f'tabuada do {numero}:')
for i in range (1 , 11):
    resultado = numero * i
    print (f'{numero} x {i:2} = {resultado} ')

print ('-'*18)
print (f'essa é a tabuada do {numero}')
print ('-' *18)

           
    

