'''
Lista de exercícios opcionais 5 - Exercício 1

---
Escreva a função n_primos que recebe como argumento um número inteiro maior ou 
igual a 2 como parâmetro e devolve a quantidade de números primos 
que existem entre 2 e n (incluindo 2 e, se for o caso, n).
---

Exemplo:
>>>n_primos(2)
1
>>>n_primos(4)
2
>>>n_primos(121)
30
'''

def is_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def n_primos(n):
    count = 0
    for num in range(2, n + 1):  
        if is_primo(num):  
            count += 1  
    return count  