# Tarefa 6: Fibonacci até N
# Código: T6
# Descrição: Crie uma função que receba um número inteiro n e retorne uma lista com todos os números da sequência de Fibonacci
# menores que n. Esse exercício envolve o cálculo e controle de recursividade ou iteração.

# Passos:
# Crie uma função chamada fibonacci_ate(n).
# A função deve gerar a sequência de Fibonacci até que o valor exceda n.
# Adicione cada número da sequência a uma lista de resultados.
# Retorne a lista de números da sequência de Fibonacci menores que n.

# Exemplos:
# Se n = 10, a função deve retornar [0, 1, 1, 2, 3, 5, 8].
# Se n = 20, a função deve retornar [0, 1, 1, 2, 3, 5, 8, 13].

def fibonacci_ate(n):
    resultados = []
    n1 = 0
    n2 = 1
    nextNumber = n1 + n2
    if (n == 0):
        resultados.append(n1)
        return resultados
    elif (n == 1):
        resultados.append(n1)
        resultados.append(n2)
        resultados.append(nextNumber)
        return resultados
    else:
        resultados.append(n1)
        resultados.append(n2)
        resultados.append(nextNumber)
        for numero in range(n):
            n1 = n2
            n2 = nextNumber
            nextNumber = n1 + n2
            if (nextNumber <= n):
                resultados.append(nextNumber)
        return resultados


lista_fibonacci = fibonacci_ate(10)

for numero in lista_fibonacci:
    print(numero, "-", end="")
