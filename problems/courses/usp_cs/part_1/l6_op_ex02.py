'''
Lista de exercícios opcionais 6 - Exercício 2

---
Como pedido na primeira video-aula desta semana, escreva um programa que recebe 
uma sequência de números inteiros e imprima todos os valores em ordem inversa. 
A sequência sempre termina pelo número 0. Note que 0 (ZERO) não deve fazer parte da sequência.
---
'''

numbers = []

while True:
    n = int(input('Digite um número: '))
    if n == 0:
        break
    numbers.append(n)

for num in reversed(numbers):
    print(num)
