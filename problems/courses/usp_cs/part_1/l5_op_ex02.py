'''
Lista de exercícios opcionais 5 - Exercício 2

---
Dizemos que um número é uma hipotenusa de um triângulo inteiro se existe um 
triângulo retângulo com lados inteiros cuja hipotenusa é igual a esse número. Em outras palavras,
h é uma hipotenusa se existem números inteiros i e j tais que:
h² = i² + j²

Escreva uma função soma_hipotenusas que receba como parâmetro um número inteiro positivo n
e devolva a soma de todos os inteiros entre 1 e n que são comprimento da hipotenusa 
de algum triângulo retângulo com catetos inteiros.
---

DIca1: um mesmo número pode ser hipotenusa de vários triângulos, 
mas deve ser somado apenas uma vez. Uma boa solução para este exercício é fazer um laço 
de 1 até n testando se o número é hipotenusa de algum triângulo e somando em caso afirmativo. 
Uma solução que dificilmente vai dar certo é fazer um laço construindo triângulos e somando as hipotenusas inteiras encontradas.

Dica2: primeiro faça uma função é_hipotenusa que diz se um número inteiro é o 
comprimento da hipotenusa de um triângulo com lados de comprimento inteiro ou não.

Exemplo:
# Para n = 25, as hipotenusas são:
# 5, 10, 13, 15, 17, 20, 25
# note que cada número deve ser somado apenas uma vez. Assim:
soma_hipotenusas(25)
# deve devolver 105
'''

def is_hipotenusa(h):
    for i in range(1, h):  
        for j in range(1, h):  
            if i**2 + j**2 == h**2:
                return True  
    return False  

def soma_hipotenusas(n):
    soma = 0
    for h in range(1, n + 1):
        if is_hipotenusa(h):  
            soma += h  
    return soma  

