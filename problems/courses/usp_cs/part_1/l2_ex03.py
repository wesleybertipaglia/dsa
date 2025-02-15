'''
Lista de exercícios 2 - Exercícios 3
Receba um número inteiro na entrada e imprima

Buzz

se o número for divisível por 5. 
Caso contrário, imprima o mesmo número que foi dado na entrada.
'''

number = int(input("Digite um numero: "))
result_Buzz = "Buzz" if (number % 5 == 0) else number
print(result_Buzz)