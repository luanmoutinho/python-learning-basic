# Tarefa 4: Soma de Números Divisíveis por 3 ou 5

# Descrição: Crie uma função que receba um número inteiro positivo n e retorne a soma de todos os números
# menores que n que sejam divisíveis por 3 ou 5. Este exercício trabalha a lógica de divisibilidade e somatórios.

# Passos:
# Crie uma função chamada soma_divisiveis(n).
# A função deve iterar sobre todos os números menores que n.
# Para cada número, verifique se é divisível por 3 ou 5.
# Some esses números e retorne o resultado final.

# Exemplos:
# Se n = 10, a função deve retornar 23, porque os números menores que 10 e divisíveis por 3 ou 5 são: 3, 5, 6, 9 (soma: 3 + 5 + 6 + 9 = 23).
# Se n = 15, a função deve retornar 45.


def soma_divisiveis(n):
    soma = 0
    for numero in range(n):
        if ((numero % 3) == 0 or (numero % 5) == 0):
            soma += numero
    return soma


print(soma_divisiveis(15))
