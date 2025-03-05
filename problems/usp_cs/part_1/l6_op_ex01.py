'''
Lista de exercícios opcionais 6 - Exercício 1

---
Escreva a função maior_elemento que recebe como parâmetro uma lista com números 
inteiros e devolve um número inteiro correspondente ao maior valor presente na lista recebida.
---
'''

def maior_elemento(lst):
    maior = lst[0]
    for n in lst:
        if n > maior:
            maior = n
    return maior