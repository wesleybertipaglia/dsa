'''
Lista de exercícios 1 - Exercício 2

---
Faça um programa em Python que receba quatro notas, calcule e imprima a média 
aritmética.
---

Exemplo:
# Entrada de Dados:
Digite a primeira nota: 4
Digite a segunda nota: 5
Digite a terceira nota: 6
Digite a quarta nota: 7

# Saída de Dados:
A média aritmética é 5.5

Dica: uso do print
Quando você usa o comando print para imprimir mais de uma coisa, ele inclui 
automaticamente espaços entre os argumentos impressos. Cuidado para não incluir 
espaços demais na sua resposta! O corretor perceberá e tirará pontos
'''

notas = []
notas.append(int(input("Digite a primeira nota: ")))
notas.append(int(input("Digite a segunda nota: ")))
notas.append(int(input("Digite a terceira nota: ")))
notas.append(int(input("Digite a quarta nota: ")))

media = sum(notas)/len(notas)

print(f"A média aritmética é {media}")