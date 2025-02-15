'''
Lista de exercícios 4 - Exercício 2
Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função

Exemplos de execução no shell do Python:
>>> maior_primo(100)
97
>>> maior_primo(7)
7
'''

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def maior_primo(n):
    for num in range(n, 1, -1):
        if is_prime(num):
            return num
