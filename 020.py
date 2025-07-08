#Exercício 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
pri = input('Primeiro aluno: ')
seg = input('Segundo aluno: ')
ter = input('Terceiro aluno: ')
qua = input('Quarto aluno: ')

alunos = [pri,seg,ter,qua]
seq = random.shuffle(alunos) #random.shuffle() = mistura a ordem de todos os elementos de uma lista existente.

print(f'A ordem de apresentação é: \n {alunos} ') 