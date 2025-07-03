'''Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
Calcule e mostre o comprimento da hipotenusa.'''

import math #biblioteca matemática

Co = float(input('Qual o comprimento do cateto oposto? '))
Ca = float(input('Qual o comprimento do cateto adjacente? '))

hip = math.hypot(Co,Ca)

print('O Valor da Hipotenusa é: {:.2f}'.format(hip))


'''Sem Importação'''
'''
Co = float(input('Qual o comprimento do cateto oposto? '))
Ca = float(input('Qual o comprimento do cateto adjacente? '))

hip = (Co**2 + Ca**2) ** (1/2)

print('O Valor da Hipotenusa é: {:.2f}'.format(hip))'''