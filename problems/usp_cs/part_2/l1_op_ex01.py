'''
Lista de exercícios Opcionais 1 - Exercício 1

Como proposto na primeira vídeo-aula da semana, escreva uma função imprime_matriz(matriz), 
que recebe uma matriz como parâmetro e imprime a matriz, linha por linha. 
Note que NÃO se deve imprimir espaços após o último elemento de cada linha!

Dica: lembre da primeira parte do curso, na semana 7! A função "print" em geral adiciona 
uma quebra de linha ao final, mas você pode controlar isso usando o argumento opcional "end"dessa forma:

>>>print("oi")
oi
>>>
>>>print("oi", end="")
oi>>>

Exemplos:
minha_matriz = [[1], [2], [3]]
imprime_matriz(minha_matriz)
1
2
3

minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha_matriz)
1 2 3
4 5 6
'''

def imprime_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j != 0:
                print(" ", end="")
            print(str(matriz[i][j]), end="")
        print() 
