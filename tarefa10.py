# Tarefa 10: Jogo da Adivinhação
# Código: T10
# Descrição: Crie uma função que implemente um simples jogo de adivinhação. A função deve escolher um número aleatório entre 1 e 100 e permitir que o usuário tente adivinhar esse número. O jogo deve fornecer feedback se o palpite foi muito alto, muito baixo ou correto. Este exercício envolve lógica de controle de fluxo e interação com o usuário.

# Passos:
# Crie uma função chamada jogo_adivinhacao().
# Utilize a biblioteca random para gerar um número aleatório entre 1 e 100.
# Inicie um loop que permita ao usuário inserir palpites até que ele acerte o número.
# Para cada palpite, forneça feedback: "muito alto", "muito baixo" ou "parabéns, você acertou!".
# Após acertar, pergunte se o usuário gostaria de jogar novamente e repita o processo se desejar.

# Exemplo de uso:
# O usuário é solicitado a adivinhar um número, e a função fornece feedback a cada palpite até que o usuário acerte.
# Se o número gerado for 42, o usuário pode tentar palpites como 30 (feedback: "muito baixo") e 50 (feedback: "muito alto"), até acertar.

import random


def jogo_adivinhacao():
    continuar = True
    tentativas = 0
    resposta = random.randint(1, 100)

    while continuar:
        palpite = int(input('Dê o seu palpite > '))
        tentativas = tentativas + 1
        if (palpite == resposta):
            print('Parabéns!, você acertou! ')
            print(f'Número de tentativas: {tentativas}')
            tentativas = 0
            proximo = input('Digite X para jogar outra vez ou 0 para sair > ')
            if (proximo == 'x' or proximo == 'X'):
                resposta = random.randint(1, 100)
            else:
                print('Obrigado por jogar!')
                continuar = False
        elif (palpite > resposta):
            print('feedback: "muito alto"')
        else:
            print('feedback: "muito baixo"')


jogo_adivinhacao()
