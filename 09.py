#Exercício 9: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Uma distância em metros: '))
km = m / 1000
cm = m * 100 
mm = m * 1000

print(f'a medida de {m}m corresponde a \n {km}Km \n {cm}cm \n {mm}mm')