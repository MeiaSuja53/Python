# Exercício 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Digite o ângulo que você deseja: '))
tomate = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(angulo, tomate))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(angulo, cos))
print('O ângulo de {:.2f} tem a TANGENTE de {:.2f}'.format(angulo, tan))