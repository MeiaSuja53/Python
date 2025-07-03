# Exercício 11: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input('Quanto de dinheiro você tem? R$ '))
dolar = real/5.40
print('Com R${} você pode comprar ${:.2f} dolares'.format(real,dolar))