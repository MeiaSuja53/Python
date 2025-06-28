# Exercício 5: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
# .Is - é um sufixo comum para vários métodos de string que retornam um valor booleano (True ou False). 
# Esses métodos são usados para verificar se uma string (ou todos os seus caracteres) satisfaz uma determinada condição.

a = input('Escreva algo: ')

#print('Qual o tipo primitivo?', type(a))
#print('Só tem espaço?', a.isspace())
#print('É um numero?', a.isnumeric())
#print('É alfabetico?', a.isalpha())
#print('É alfanumerico?', a.isalnum())
#print('Esta em maiusculas?', a.isupper())
#print('Esta em minusculas?', a.islower())
#print('Esta capitalizada', a.istitle())

print (f'Qual o tipo primitivo?{type(a)}, Só tem espaço? {a.isspace()}, É um numero? {a.isnumeric()}, É alfabetico? {a.isalpha()}, ' \
f'É alfanumerico? {a.isalnum()}, Esta em maiusculas? {a.isupper()}, Esta em minusculas? {a.islower()}, Esta capitalizada? {a.istitle()}')