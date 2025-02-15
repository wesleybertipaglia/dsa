'''
Lista de exercícios 3 - Exercício 1
Escreva um programa que receba um número natural n na entrada e imprima n! (fatorial) na saída.

Exemplo:
Digite o valor de n: 5
120

Dica: lembre-se que o fatorial de 0 vale 1!
'''

def factorial(n):
    if n < 0:
        raise ValueError("O fatorial não é definido para números negativos.")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

n = int(input('Digite o valor de n: '))

try:
    result = factorial(n)
    print(result)
except ValueError as e:
    print(e)
