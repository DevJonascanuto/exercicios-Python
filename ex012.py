# faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% DE DESCONTOs
preco = float (input('digite o valor do produto'))
Pdesc = float (preco * 0.05) 
Pfinal = float (preco - Pdesc)
print (f'o valor final do produto com desconto é {Pfinal:.2f}')
  
