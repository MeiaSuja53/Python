# Exercício 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual o salario atual do funcionario? R$ '))
novo = salario + (salario*15/100)

print('O funcionario que recebia {:.2f}, agora passa a receber {:.2f}.'.format(salario,novo))