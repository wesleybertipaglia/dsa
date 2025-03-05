'''
Lista de exercícios 1 - Exercício 2

Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve uma matriz que 
represente sua soma caso as matrizes tenham dimensões iguais. Caso contrário, a função deve devolver False.

Exemplos:
m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
soma_matrizes(m1, m2) => [[3, 5, 7], [9, 11, 13]]

m1 = [[1], [2], [3]]
m2 = [[2, 3, 4], [5, 6, 7]]
soma_matrizes(m1, m2) => False
'''

def soma_matrizes(m1, m2):
    dx_m1 = len(m1[0])    
    dy_m1 = len(m1)

    dx_m2 = len(m2[0])
    dy_m2 = len(m2)

    if (dx_m1 != dx_m2 or dy_m1 != dy_m2):
        return False

    for x in range(len(m1)):
        for j in range(len(m1[0])):
            m1[x][j] += m2[x][j]

    return m1
