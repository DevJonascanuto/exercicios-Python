''' escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelo quais ele foi alugado. calcule
o preço a pagar sabendo que o carro custa r$ 60.00 POR DIA e r$ 0.15 CENTAVOS POR KM RODADO '''
# requisitos preço do KM = R$ 0,15 
# VALOR DA DIARIA R$ 60,00



km = float (input('quantos Kms foram rodados ?'))
diaria = int (input('Quantos dias de aluguel do veiculo ?'))
cobrar = km * 0.15 + diaria * 60
print (f'foram rodados {km:.2f} Kms e a locação foi de {diaria} dias, o valor total a ser cobrado é de {cobrar:.2f} R$')





