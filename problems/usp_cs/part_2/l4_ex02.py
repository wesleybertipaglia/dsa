'''
Lista de exercícios 4 - Exercício 2

Implemente a função busca(lista, elemento), que busca um determinado elemento em 
uma lista e devolve o índice correspondente à posição do elemento encontrado. 
Utilize o algoritmo de busca sequencial. Nos casos em que o elemento buscado não existir na lista, a função deve devolver o booleano False.

Exemplo:
'''

def busca(lista, elemento):
    left, right = 0, len(lista) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if lista[mid] == elemento:
            return mid
        elif lista[mid] < elemento:
            left = mid + 1
        else:
            right = mid - 1

    return False

