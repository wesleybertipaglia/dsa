'''
Lista de exercícios 2 - Exercícios 2
Receba um número inteiro na entrada e imprima 

Fizz

se o número for divisível por 3. Caso contrário, 
imprima o mesmo número que foi dado na entrada.
'''

number = int(input("Digite um numero: "))
result_fizz = "Fizz" if (number % 3 == 0) else number
print(result_fizz)