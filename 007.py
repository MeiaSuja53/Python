#Exercício 07: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
num = int(input('Digite um numero: '))
do = num * 2
tri = num * 3
qua = num ** (1/2) 

print(num)
print(f'O dobro de: {num} vale {do}.')
print(f'O triplo de: {num} vale {tri}.')
print('A raiz quadrada de: {} vale {:.2f}.'.format(num, qua))