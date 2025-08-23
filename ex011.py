''' faça um programa qye leia a largura e a altura de uma parede em metros e calcule 
sua area e a quantidade de tinta nescessaria para pintala sabendo que a cada litro de tinta pinta 2m
'''
altura = float (input('vou calcular quantos m² tem sua parede, digite a altura em METROS'))
largura = float (input(' agora digite a largura da parede'))
area = altura * largura
litros = area / 2
print (f'a sua parede tem {area} m² voce precisa de {litros:.2f} litros, para pintala por completo.') 