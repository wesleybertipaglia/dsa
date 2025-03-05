'''
Lista de exercícios 6 - Exercício 2

Implemente a função encontra_impares(lista), que recebe como parâmetro uma lista de números 
inteiros e devolve uma outra lista apenas com os números ímpares da lista dada.

Sua solução deve ser implementada utilizando recursão.

Dica: você vai precisar do método extend() que as listas possuem.
'''

def encontra_impares(lista):
    if not lista:
        return []
    else:
        if lista[0] % 2 != 0:
            return [lista[0]] + encontra_impares(lista[1:])
        else:
            return encontra_impares(lista[1:])
