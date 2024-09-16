# Tarefa 5: Números Primos em um Intervalo
# Código: T5
# Descrição: Crie uma função que receba dois números inteiros positivos a e b,
#  e retorne uma lista com todos os números primos entre a e b (inclusive).
# Esse exercício trabalha a lógica de verificação de números primos e manipulação de listas.

# Passos:
# Crie uma função chamada numeros_primos(a, b).
# A função deve iterar sobre todos os números entre a e b.
# Para cada número, verifique se é primo.
# Se for primo, adicione-o à lista de resultados.
# Retorne a lista de números primos.

# Exemplos:
# Se a = 10 e b = 20, a função deve retornar [11, 13, 17, 19].
# Se a = 1 e b = 10, a função deve retornar [2, 3, 5, 7].


num_inicial = int(input("Digite o primeiro numero: > "))
num_final = int(input("Digite o primeiro numero: > "))


def numeros_primos(a, b):
    primos = []
    for numero in range(a, b):
        if (numero == 2 or numero == 3):
            primos.append(numero)
        elif (numero > 3 and numero % 2 != 0 and numero % 3 != 0):
            primos.append(numero)
        else:
            continue

    return primos


primos = numeros_primos(num_inicial, num_final)

for numero in primos:
    print(numero, " - ", end="")
