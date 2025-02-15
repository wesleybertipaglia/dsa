'''
Lista de exercícios opcionais 3 - Exercício 2
Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido 
possui ao menos um dígito com um dígito adjacente igual a ele. 
Caso exista, imprima "sim"; se não existir, imprima "não".

Exemplos:
Digite um número inteiro: 12345
não

Digite um número inteiro: 1011
sim
'''

def verify_numbers(n):
    for i in range(1, len(n)):
        if n[i] == n[i - 1]:
            return print("sim")
    print("não")

n = input("Digite um número inteiro: ")
verify_numbers(n)
