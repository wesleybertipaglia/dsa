'''
Lista de exercícios 4 - Exercício 1

---
Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.
---

Exemplos de execução no shell do Python:
>>> maximo(3, 4)
4
>>> maximo(0, -1)
0
'''

def maximo(n1, n2):
    return n1 if (n1 > n2) else n2