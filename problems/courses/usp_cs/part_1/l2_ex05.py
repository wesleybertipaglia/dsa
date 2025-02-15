'''
Lista de exercícios 2 - Exercícios 5
Receba 3 números inteiros na entrada e imprima:

crescente
se eles forem dados em ordem crescente. 

Caso contrário, imprima:
não está em ordem crescente
'''

first_number = int(input("Digite o 1º número: "))
result = "crescente"

last_number = first_number
for x in range(2):
    current_number = int(input(f"Digite o {x+1}º numero: "))
    if (current_number < last_number):
        result = "não está em ordem crescente"
    last_number = current_number

print(result)