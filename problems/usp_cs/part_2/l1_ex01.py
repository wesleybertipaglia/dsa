'''
Lista de exercícios 1 - Exercício 1

Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e 
imprime as dimensões da matriz recebida, no formato iXj.

Exemplos:
minha_matriz = [[1], [2], [3]]
dimensoes(minha_matriz)
3X1

minha_matriz = [[1, 2, 3], [4, 5, 6]]
dimensoes(minha_matriz)
2X3
'''

def dimensoes(matriz):
    if not matriz or not matriz[0]:
        print("0X0")
    print(f"{len(matriz)}X{len(matriz[0])}")

