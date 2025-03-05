'''
Lista de exercícios Opcionais 1 - Exercício 2

Este é o desafio do vídeo "Entrada de Dados".

Reescreva o programa contaSegundos para imprimir também a quantidade de dias, 
ou seja, faça um programa em Python que, dada a quantidade de segundos, 
"quebre" esse valor em dias, horas, minutos e segundos. A saída deve estar no 
formato: a dias, b horas, c minutos e d segundos. Seja cuidadoso com o formato! 
Espaços a mais, vírgulas faltando ou outras diferenças são considerados erro.

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:
# Entrada de Dados:
Por favor, entre com o número de segundos que deseja converter: 178615

# Saída de Dados:
2 dias, 1 horas, 36 minutos e 55 segundos.
'''

seconds = int(input('Por favor, entre com o número de segundos que deseja converter: '))
const_day_seconds = 24 * 60 * 60
const_hours_seconds = 60 * 60
const_minutes_seconds = 60
const_seconds = 1

def get_result_by_seconds(value):
    global seconds
    result = seconds // value
    seconds %= value
    return result

result_days = get_result_by_seconds(const_day_seconds)
result_hours = get_result_by_seconds(const_hours_seconds)
result_minutes = get_result_by_seconds(const_minutes_seconds)
result_seconds = get_result_by_seconds(const_seconds)

print(f'{result_days} dias, {result_hours} horas, {result_minutes} minutos e {result_seconds} segundos.')