from random import randint


def mensagem_tela(mensagem):
    print('-' * 50)
    print(f'{mensagem.upper():^50}')
    print('-' * 50)


def recebe_numero_jogador():
    return int(input('Digite um número entre 0 e 10: '))


def valida_tentativa_jogador(numero):
    return numero in range(11)


def verifica_acerto(numero_jogador, numero_computador):
    return numero_jogador == numero_computador


numero_computador = randint(0, 11)
numero_jogador = int()
rodada = 1

TENTATIVAS = 5
MENSAGEM_SAUDACAO = 'Escolhi um número entre 0 e 10. Tente adivinhar'
MENSAGEM_VITORIA = 'Parabéns!! Você acertou'
MENSAGEM_DERROTA = 'Que pena!! Você não acertou'
MENSAGEM_NUMERO_INVALIDO = 'ERRO: Número fora da faixa permitida'

mensagem_tela(MENSAGEM_SAUDACAO)
while rodada < TENTATIVAS + 1:
    print(f'Rodada {rodada}/{TENTATIVAS}')
    numero_jogador = recebe_numero_jogador()

    while not valida_tentativa_jogador(numero_jogador):
        mensagem_tela(MENSAGEM_NUMERO_INVALIDO)
        print(f'Rodada {rodada}/{TENTATIVAS}')
        numero_jogador = recebe_numero_jogador()

    if verifica_acerto(numero_jogador, numero_computador):
        mensagem_tela(MENSAGEM_VITORIA)
        break

    rodada += 1

    if rodada == TENTATIVAS + 1:
        mensagem_tela(MENSAGEM_DERROTA)
