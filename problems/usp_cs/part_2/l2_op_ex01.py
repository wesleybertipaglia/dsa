'''
Lista de exercícios Opcionais 2 - Exercício 1

Escreva a função conta_letras(frase, contar="vogais"), que recebe como primeiro parâmetro uma string 
contendo uma frase e como segundo parâmetro uma outra string. Este segundo parâmetro deve ser opcional.

Quando o segundo parâmetro for definido como "vogais", a função deve devolver o numero de vogais presentes na frase. 
Quando ele for definido como "consoantes", a função deve devolver o número de consoantes presentes na frase. 
Se este parâmetro não for passado para a função, deve-se assumir o valor "vogais" para o parâmetro.

Exemplos:
conta_letras('programamos em python')
# deve devolver 6

conta_letras('programamos em python', 'vogais')
# deve devolver 6

conta_letras('programamos em python', 'consoantes')
# deve devolver 13
'''

def conta_letras(frase, contar="vogais"):
    vogais = ['a', 'e', 'i', 'o', 'u']
    frase = frase.lower()
    contador = 0

    for letra in frase:
        if letra.isalpha():
            if contar == "vogais":
                if letra in vogais:
                    contador += 1
            elif contar == "consoantes":
                if letra not in vogais:
                    contador += 1

    return contador
