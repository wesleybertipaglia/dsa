'''
Lista de exercícios 2 - Exercício 1

Receba um número inteiro na entrada e imprima:
par quando o número for par ou, ímpar quando o número for ímpar.
'''

number = int(input("Digite um numero: "))
result_even_odd = "par" if (number % 2 == 0) else "ímpar"
print(result_even_odd)