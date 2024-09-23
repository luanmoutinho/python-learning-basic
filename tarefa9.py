# Tarefa 9: Contagem de Vogais e Consoantes
# Código: T9
# Descrição: Crie uma função que receba uma string e retorne um dicionário com a contagem de vogais e consoantes na string.
# Este exercício envolve manipulação de strings e uso de dicionários.

# Passos:
# Crie uma função chamada contar_vogais_consoantes(s).
# Inicialize um dicionário com chaves "vogais" e "consoantes", ambas iniciando com valor 0.
# Itere sobre cada caractere na string, ignorando espaços e caracteres especiais.
# Para cada caractere, verifique se é uma vogal (a, e, i, o, u) ou uma consoante.
# Atualize o dicionário com a contagem correspondente.
# Retorne o dicionário.

# Exemplos:
# Se a string for "Python é incrível", a função deve retornar {"vogais": 6, "consoantes": 10}.
# Se a string for "Hello World!", a função deve retornar {"vogais": 3, "consoantes": 7}.

consoantes = (
    'B', 'b', 'C', 'c', 'D', 'd', 'F', 'f', 'G', 'g',
    'H', 'h', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm',
    'N', 'n', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's',
    'T', 't', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y',
    'Z', 'z'
)

vogais = (
    'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u',
    'Á', 'á', 'É', 'é', 'Í', 'í', 'Ó', 'ó', 'Ú', 'ú',
    'Â', 'â', 'Ê', 'ê', 'Î', 'î', 'Ô', 'ô', 'Û', 'û',
    'Ã', 'ã', 'Õ', 'õ', 'Ä', 'ä', 'Ë', 'ë', 'Ï', 'ï',
    'Ö', 'ö', 'Ü', 'ü'
)

palavra1 = 'Python é incrível'
palavra2 = 'Hello World!'
letras = {'vogais': 0, 'consoantes': 0}


def contar_vogais_consoantes(s):
    for caracter in s:
        if caracter in consoantes:
            letras['consoantes'] = letras['consoantes'] + 1
        elif caracter in vogais:
            letras['vogais'] = letras['vogais'] + 1
    return letras


print(contar_vogais_consoantes(palavra2))
