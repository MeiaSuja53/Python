#Exercício 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math #biblioteca matemática

n = float(input('Digite um numero: '))

print('O valor digitado foi: {}, e a sua porção inteira é: {}'.format(n, math.floor(n)))

#******Sem importação********
'''
n = float(input('Digite um valor: '))

print('O valor digitado foi: {}, sua parte inteira é: {}'.format(n, int(n)))'''