'''
Lista de exercícios Opcionais 6 - Exercício 2

Implemente a função fatorial(x), que recebe como parâmetro um número 
inteiro e devolve um número inteiro correspondente ao fatorial de x.

Sua solução deve ser implementada utilizando recursão.
'''

def fatorial(x):
    if x == 0:
        return 1
    else:
        return x * fatorial(x - 1)
