'''
Lista de exercícios 6 - Exercício 1

---
Escreva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, 
verifica se tal lista possui elementos repetidos e os remove. A função deve devolver 
uma lista correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.
---

Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?
'''

def remove_repetidos(lst):
    return sorted(list(set(lst)))