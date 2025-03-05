'''
Lista de exercícios 2 - Exercícios 4
Receba um número inteiro na entrada e imprima

FizzBuzz

na saída se o número for divisível por 3 e por 5. 
Caso contrário, imprima o mesmo número que foi dado na entrada.
'''

number = int(input("Digite um numero: "))
result_FizzBuzz = "FizzBuzz" if (number % 3 == 0 and number % 5 == 0) else number
print(result_FizzBuzz)