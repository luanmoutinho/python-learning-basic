from collections import Counter

lista = [4, 5, 6, 5, 4, 3, 5]
contagem = Counter(lista)
lista_repetidos = []
contagem2 = Counter(lista_repetidos)
lista_nao_repetidos = []


for item in lista:
    if (contagem[item] > 1):
        lista_repetidos.append(item)
    else:
        lista_nao_repetidos.append(item)

lista_organizada = sorted(
    lista_repetidos, key=lambda x: (-contagem2[x], x)) + sorted(lista_nao_repetidos)


lista_organizada = sorted(lista_repetidos, key=lambda x: (-contagem2[x], x)) + sorted
print(lista_organizada)
