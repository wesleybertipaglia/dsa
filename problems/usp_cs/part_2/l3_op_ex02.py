'''
Lista de exercícios Opcionais 3 - Exercício 2

Ainda na classe Triangulo, escreva um método semelhantes(triangulo) que recebe um objeto do tipo 
Triangulo como parâmetro e verifica se o triângulo atual é semelhante ao triângulo passado como parâmetro. 
Caso positivo, o método deve devolver True. Caso negativo, deve devolver False

Um triângulo é semelhante a outro triângulo se a razão (divisão) entre os comprimentos dos seus lados forem iguais.

Dica: você pode colocar os lados de cada um dos triângulos em uma lista diferente e ordená-las.

Exemplo:
t1 = Triangulo(2, 3, 5)
t2 = Triangulo(4, 6, 10)
t1.semelhantes(t2)
# deve devolver True
'''

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c
    
    def semelhantes(self, triangulo):
        lados_self = sorted([self.a, self.b, self.c])
        lados_triangulo = sorted([triangulo.a, triangulo.b, triangulo.c])

        if lados_triangulo[0] == 0:
            return False
        razao = lados_self[0] / lados_triangulo[0]

        for i in range(1, 3):
            if lados_triangulo[i] == 0 or lados_self[i] / lados_triangulo[i] != razao:
                return False

        return True
