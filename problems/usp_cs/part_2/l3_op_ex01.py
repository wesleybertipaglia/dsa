'''
Lista de exercícios Opcionais 3 - Exercício 1

Escreva, na classe Triangulo, o método retangulo() que devolve True se o triângulo for retângulo, e False caso contrário.

Exemplos:
t = Triangulo(1, 3, 5)
t.retangulo()
# deve devolver False

u = Triangulo(3, 4, 5)
u.retangulo()
# deve devolver True
'''

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def retangulo(self):
        return (self.a**2) + (self.b**2) == (self.c**2)
