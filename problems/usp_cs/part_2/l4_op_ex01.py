'''
Lista de exercícios Opcionais 4 - Exercício 1

Escreva a função lista_grande(n), que recebe como parâmetro um número inteiro n e 
devolve uma lista contendo n números inteiros aleatórios.
'''

import random

def lista_grande(n):
    lista = []
    for x in range(n):
        num = random.randint(0,99)
        lista.append(num)
    return lista