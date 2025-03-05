'''
Lista de exercícios Opcionais 2 - Exercício 2
Como pedido na videoaula desta semana, escreva um programa que calcula as raízes 
de uma equação do segundo grau.

O programa deve receber os parâmetros a, b, e c da equação ax²+bx+c, 
respectivamente, e imprimir o resultado na saida da seguinte maneira:

Quando não houver raízes reais imprima:

esta equação não possui raízes reais

Quando houver apenas uma raiz (ou seja, uma raiz com multiplicidade 2) imprima:

a raiz desta equação é X

ou onde X é o valor da raiz dupla:

a raiz dupla desta equação é X

Quando houver duas raízes reais imprima:

as raízes da equação são X e Y

Além disso, no caso de existirem 2 raízes reais distintas, elas devem ser impressas em ordem crescente. Exemplos:

as raízes da equação são 1.0 e 2.0

as raízes da equação são -2.0 e 0.0
'''

import math

a = int(input("Digite a: "))
b = int(input("Digite b: "))
c = int(input("Digite c: "))

discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("esta equação não possui raízes reais")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"a raiz dupla desta equação é {root}")
else:
    sqrt_discriminant = math.sqrt(discriminant)
    root1 = (-b + sqrt_discriminant) / (2*a)
    root2 = (-b - sqrt_discriminant) / (2*a)
    
    if root1 > root2:
        root1, root2 = root2, root1
    print(f"as raízes da equação são {root1} e {root2}")
