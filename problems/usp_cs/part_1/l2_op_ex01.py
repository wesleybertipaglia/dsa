'''
Lista de exercícios Opcionais 2 - Exercício 1
Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, 
respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. 
Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de 
um outro ponto no mesmo plano.

Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10,
imprima:

longe

na saída. Caso o contrário, quando a distância for menor que 10, imprima

perto


Dica: lembre-se que a fórmula da distância para dois pontos num plano cartesiano é a seguinte:
d(x,y) = √((x1 - x2)² + (y1 - y2)²)
'''

import math

x1 = int(input('Digite o x1: '))
y1 = int(input('Digite o y1: '))

x2 = int(input('Digite o x2: '))
y2 = int(input('Digite o y2: '))

distancia = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
result = "perto" if (distancia <= 10) else "longe"

print(result)