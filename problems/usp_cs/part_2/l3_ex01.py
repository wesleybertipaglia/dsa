'''
Lista de exercícios 3 - Exercício 1

Defina a classe Triangulo cujo construtor recebe 3 valores inteiros correspondentes aos lados a, b e c de um triângulo.

A classe triângulo também deve possuir um método perimetro, que não recebe parâmetros e 
devolve um valor inteiro correspondente ao perímetro do triângulo.

Exemplos:
t = Triangulo(1, 1, 1)
# deve atribuir uma referência para um triângulo de lados 1, 1 e 1 à variável t 

Um objeto desta classe deve responder às seguintes chamadas:
t.a
# deve devolver o valor do lado a do triângulo
t.b
# deve devolver o valor do lado b do triângulo
t.c
# deve devolver o valor do lado c do triângulo

t.perimetro()
# deve devolver um inteiro correspondente ao valor do perímetro do triângulo.
'''

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c
