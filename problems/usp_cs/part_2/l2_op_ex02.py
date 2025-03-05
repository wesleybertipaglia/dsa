'''
Lista de exercícios Opcionais 2 - Exercício 2

Como pedido no segundo vídeo da semana, escreva a função primeiro_lex(lista) que recebe uma lista de strings 
como parâmetro e devolve o primeiro string na ordem lexicográfica. Neste exercício, considere letras maiúsculas e minúsculas.

Dica: revise a segunda vídeo-aula desta semana.

Exemplos:
primeiro_lex(['oĺá', 'A', 'a', 'casa'])
# deve devolver 'A'

primeiro_lex(['AAAAAA', 'b'])
# deve devolver 'AAAAAA'
'''

def primeiro_lex(lista):
    primeira_string = lista[0]

    for i in lista:
        if (i < primeira_string):
            primeira_string = i

    return primeira_string
