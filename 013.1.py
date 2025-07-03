#Exercício 13.1: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Informe a temperatura em °C: '))
f = celsius * 9/5 + 32

print('A temperatura de {} em °C, é equivalente a {} °F!'.format(celsius,f))