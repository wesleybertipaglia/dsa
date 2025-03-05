'''
Lista de exercícios opcionais 3 - Exercício 1
Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. 
Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".
'''

def is_prime(n, divisor=2):
    if n < 2:
        return False

    if divisor * divisor > n:  
        return True

    if n % divisor == 0:
        return False

    return is_prime(n, divisor + 1)

n = int(input("Digite um número inteiro: "))
print("primo" if is_prime(n) else "não primo")
