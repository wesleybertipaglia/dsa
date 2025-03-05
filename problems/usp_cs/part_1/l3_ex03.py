'''
Lista de exercícios 3 - Exercício 3
Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

Exemplo:
Digite um número inteiro: 123
6
'''

def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)

n = int(input('Digite um número inteiro: '))
print(sum_digits(abs(n)))
