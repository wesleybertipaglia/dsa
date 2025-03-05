'''
Lista de exercícios 5 - Exercício 1

Implemente a função busca(lista, elemento), que busca um determinado elemento em uma lista e devolve 
o índice correspondente à posição do elemento encontrado. Utilize o algoritmo de busca binária. 
Nos casos em que o elemento buscado não existir na lista, a função deve devolver o booleano False.

Além de devolver o índice correspondente à posição do elemento encontrado, sua função deve imprimir cada um dos índices testados pelo algoritmo.

Exemplo:
busca(['a', 'e', 'i'], 'e')
1
# deve devolver => 1

busca([1, 2, 3, 4, 5], 6)
2
3
4
# deve devolver => False

busca([1, 2, 3, 4, 5, 6], 4)
2
4
3
# deve devolver => 3
'''

def busca(lista, elemento):
    left, right = 0, len(lista) - 1

    while left <= right:
        mid = left + (right - left) // 2
        print(mid)

        if lista[mid] == elemento:
            return mid
        elif lista[mid] < elemento:
            left = mid + 1
        else:
            right = mid - 1

    return False
