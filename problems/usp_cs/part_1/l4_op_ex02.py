'''
Lista de exercícios opcionais 4 - Exercício 2

---
Reescreva a função 'maximo' do outro exercício, 
que devolve o maior valor dentre dois inteiros recebidos, 
para que ela passe a receber 3 valores inteiros como parâmetros e devolva o maior dentre eles.
---

Exemplos de execução no Python Shell
>>>maximo(30, 14, 10)
30
>>>maximo(0, -1, 1)
1
'''

def maximo(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3
