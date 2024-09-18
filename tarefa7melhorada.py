

from collections import Counter

# uma outra altenativa de código seria usando diretamente a classe Counter para fazer a contagem dos itens da lista original
# e retornar uma uma lista com os filtros de frequencia usando o metodo sorted com uma função lambda
# Nesta versão o código fica menos robusto

lista = [4, 5, 6, 5, 4, 3]


def ordenar_por_frequencia(lista):
    contagem = Counter(lista)

    lista_organizada = sorted(lista, key=lambda x: (-contagem[x], x))
    return lista_organizada


print(ordenar_por_frequencia(lista))
