'''
Lista de exercícios Opcionais 4 - Exercício 2

Implemente a função ordena(lista), que recebe uma lista com números inteiros como parâmetro 
e devolve esta lista ordenada em ordem crescente. Utilize o algoritmo selection sort.
'''

def ordena(lista):
    for i in range(len(lista)):
        min = i
        
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min]:
                min = j
        
        lista[i], lista[min] = lista[min], lista[i]
    
    return lista
