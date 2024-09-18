# Tarefa 7: Ordenação por Frequência
# Código: T7
# Descrição: Crie uma função que receba uma lista de números inteiros e retorne essa lista ordenada pela frequência de cada número.
#  Números com maior frequência devem aparecer primeiro e, em caso de empate,
# o número menor deve vir antes. Esse exercício trabalha a lógica de contagem e ordenação.

# Passos:
# Crie uma função chamada ordenar_por_frequencia(lista).
# Conte quantas vezes cada número aparece na lista.
# Ordene a lista de acordo com a frequência dos números.
# Em caso de empate de frequência, ordene os números em ordem crescente.

# Exemplos:
# Se a lista for [4, 5, 6, 5, 4, 3], a função deve retornar [4, 4, 5, 5, 3, 6].
# Se a lista for [1, 1, 2, 2, 3], a função deve retornar [1, 1, 2, 2, 3].


from collections import Counter

lista = [4, 5, 6, 5, 4, 3]


def ordenar_por_frequencia(lista):

    # cria um dicionário onde as chaves são os elementos da coleção,
    # e os valores são as quantidades de vezes que esses elementos aparecem.
    contagem = Counter(lista)

    lista_repetidos = []
    lista_nao_repetidos = []

    for item in lista:

        if (contagem[item] > 1):

            lista_repetidos.append(item)

        else:

            lista_nao_repetidos.append(item)

    contagem_repetidos = Counter(lista_repetidos)

    # criando uma função anônima que verrifca o itens que se repetem ordena de acordo com sua frequência
    # caso haja empate ele mantem o padrão do sorted que é a ordem crescente
    lista_organizada = sorted(
        lista_repetidos, key=lambda x: (-contagem_repetidos[x], x)) + sorted(lista_nao_repetidos)

    return (lista_organizada)


print(ordenar_por_frequencia(lista))
