from random import randint

numero_computador = randint(0, 10)
numero_jogador = None
rodada = 1

TENTATIVAS = 6
TOTAL_RODADAS = TENTATIVAS - 1
MENSAGENS = {
    'DEFAULT': {
        'SAUDACAO': 'Escolhi um número entre 0 e 10. Tente adivinhar',
        'VITORIA': 'Parabéns!! Você acertou',
        'DERROTA': 'Que pena!! Você não acertou',
        'INPUT_JOGADOR': 'Digite um número entre 0 e 10: ',
    },
    'ERRO': {
        'INPUT_INVALIDO': 'ERRO: São permitidos apenas números inteiros entre 0 e 10',
    }
}


def mensagem_tela(mensagem, pontuacao=None):
    TAMANHO_LINHA = 70
    print(f'{"-" * TAMANHO_LINHA}')
    print(f'{mensagem.upper():^70}')
    if pontuacao is not None:
        print(f'{"A SUA PONTUAÇÃO FINAL É: " + str(pontuacao) + " PONTOS":^70}')
    print(f'{"-" * TAMANHO_LINHA}')


def recebe_numero_jogador(mensagem):
    return str(input(mensagem))


def valida_input_jogador(numero):
    try:
        int(numero)
    except ValueError:
        return False
    return int(numero) in range(11)


def verifica_acerto(numero_jogador, numero_computador):
    return int(numero_jogador) == numero_computador


def calcula_pontuacao(rodada, tentativas):
    PONTUACAO_MAXIMA = 100
    if rodada == 1:
        return PONTUACAO_MAXIMA
    else:
        return PONTUACAO_MAXIMA - (PONTUACAO_MAXIMA / (tentativas - 1)) * (rodada - 1)


mensagem_tela(MENSAGENS.get('DEFAULT').get('SAUDACAO'))
print(numero_computador)
while rodada < TENTATIVAS:
    print(f'Rodada {rodada}/{TOTAL_RODADAS}')
    numero_jogador = recebe_numero_jogador(MENSAGENS.get('DEFAULT').get('INPUT_JOGADOR'))

    while not valida_input_jogador(numero_jogador):
        mensagem_tela(MENSAGENS.get('ERRO').get('INPUT_INVALIDO'))
        print(f'Rodada {rodada}/{TOTAL_RODADAS}')
        numero_jogador = recebe_numero_jogador(MENSAGENS.get('DEFAULT').get('INPUT_JOGADOR'))

    if verifica_acerto(numero_jogador, numero_computador):
        break

    rodada += 1

pontos = calcula_pontuacao(rodada, TENTATIVAS)

if rodada < TENTATIVAS:
    mensagem_tela(MENSAGENS.get('DEFAULT').get('VITORIA'), pontos)
else:
    mensagem_tela(MENSAGENS.get('DEFAULT').get('DERROTA'), pontos)
