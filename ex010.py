# crieum programa que leia quano dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
# requisitos : 1 dolar = 3,27 r$

dinheiro = float (input('digite quanto dinheiro voce tem na carteira, que eu te digo quantos dolares consegue comprar'))
print (f'voçê tem R$ {dinheiro:.2f} , vou calcular quantos dolares pode voce pode comprar. ')
dolar = (dinheiro / 3.27)
print (f'voce pode comprar {dolar:.2f} dolares com {dinheiro} reais')

