'''
Lista de exercícios 6 - Exercício 2

---
Escreva a função soma_elementos que recebe como parâmetro uma lista com 
números inteiros e devolve um número inteiro correspondente à soma dos elementos da lista recebida.
---
'''

def soma_elementos(lst):
    total = 0
    for num in lst:
        total += num
    return total