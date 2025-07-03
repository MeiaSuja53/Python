#Exercício 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
produto = float(input('Quanto custa o produto? R$ '))
desconto = produto - (produto * 5/100)

print('Com o desconto sua compra de {:.2f}, ficou {:.2f}'.format(produto,desconto))