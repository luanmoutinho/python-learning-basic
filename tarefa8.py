# Tarefa 8: Palíndromos em uma Lista
# **Código:** T8
# **Descrição:** Crie uma função que receba uma lista de strings e retorne uma nova lista contendo apenas os elementos que são palíndromos. Este exercício trabalha a lógica de verificação de palíndromos e manipulação de listas.

# **Passos:**
# 1. Crie uma função chamada `filtrar_palindromos(lista)`.
# 2. A função deve iterar sobre cada string na lista.
# 3. Para cada string, verifique se ela é um palíndromo (ou seja, se a string lida de trás para frente é igual à string original).
# 4. Se for um palíndromo, adicione à lista de resultados.
# 5. Retorne a lista de palíndromos.

# **Exemplos:**
# - Se a lista for `["ana", "bola", "radar", "python", "level"]`, a função deve retornar `["ana", "radar", "level"]`.
# - Se a lista for `["carro", "reviver", "sol", "oso"]`, a função deve retornar `["reviver", "oso"]`.

lista = ["carro", "reviver", "sol", "oso"]
palindromos = []


def filtrar_palindromos(lista):

    for palavra in lista:
        if (palavra[::-1] == palavra):
            palindromos.append(palavra)
        else:
            continue
    return palindromos


print(filtrar_palindromos(lista))
