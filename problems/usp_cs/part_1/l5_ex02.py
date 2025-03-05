'''
Lista de exercícios 5 - Exercício 2

---
Refaça o exercício 1 imprimindo os retângulos sem preenchimento, 
de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.
---

digite a largura: 10
digite a altura: 3
##########
#        #
##########

digite a largura: 2
digite a altura: 2
##
##
'''

l = int(input('digite a largura: '))
a = int(input('digite a altura: '))

print('#' * l)

for _ in range(a - 2):
    print('#' + ' ' * (l - 2) + '#') if l > 1 else print('#')

if a > 1:
    print('#' * l)
