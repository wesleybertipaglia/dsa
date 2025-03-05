'''
Lista de exercícios 4 - Exercício 1

Escreva a função ordenada(lista), que recebe uma lista com números inteiros como parâmetro
e devolve o booleano True se a lista estiver ordenada e False se a lista não estiver ordenada.
'''

def ordenada(lista):
    menor = lista[0]

    for x in lista:
        if (menor > x):
            return False
    return True