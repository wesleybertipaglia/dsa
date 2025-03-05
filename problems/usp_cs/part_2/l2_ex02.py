'''
Lista de exercícios 2 - Exercício 2

Como pedido no primeiro vídeo desta semana, escreva uma função menor_nome(nomes) que recebe 
uma lista de strings com nome de pessoas como parâmetro e devolve o nome mais curto presente na lista.

A função deve ignorar espaços antes e depois do nome e deve devolver o menor nome presente na lista. 
Este nome deve ser devolvido com a primeira letra maiúscula e seus demais caracteres minúsculos, independente 
de como tenha sido apresentado na lista passada para a função.

Quando houver mais de um nome com o menor comprimento dentre os nomes na lista, a função deve devolver o 
primeiro nome com o menor comprimento presente na lista.

Exemplos:
menor_nome(['maria', 'josé', 'PAULO', 'Catarina'])
# deve devolver 'José'

menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  '])
# deve devolver 'José'

menor_nome(['Bárbara', 'JOSÉ  ', 'Bill'])
# deve devolver José
'''

def menor_nome(nomes):
    menor_nome = nomes[0].strip()
    
    for n in nomes:
        if (len(n.strip()) < len(menor_nome)):
            menor_nome = n.strip()
    return menor_nome.capitalize()
