'''
Lista de exercícios 4 - Exercício 3
Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.

Exemplos de execução no shell de Python
>>> vogal("a")
True
>>> vogal("b")
False
>>> vogal("E")
True
'''

vogals = {'a', 'e', 'i', 'o', 'u'}

def vogal(l):
    return l.lower() in vogals
