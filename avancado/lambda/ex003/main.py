"""
Ao remover o comentário da operação POTÊNCIA, o sistema fará a inclusão automática no menu,
no cálculo e no resultado
"""
OPERACOES = {
    'soma': lambda n1, n2: n1 + n2,
    'subtração': lambda n1, n2: n1 - n2,
    'multiplicação': lambda n1, n2: n1 * n2,
    'divisão': lambda n1, n2: n1 / n2,
    # 'potência': lambda n1, n2: n1 ** n2,
}
nome_operacao = lambda operacao: list(OPERACOES.keys())[operacao - 1]
lista_operacoes = list(OPERACOES.keys())
total_operacoes = len(OPERACOES) + 1


def mensagem_operacoes():
    print('Operações:')
    for i, j in enumerate(lista_operacoes):
        print(f' ({i + 1}) {j.title()}')
    print('')


def operacao_valida(operacao):
    return operacao in range(1, total_operacoes)


def efetua_operacao(operacao, numero1, numero2):
    calculo = OPERACOES.get(nome_operacao(operacao))
    return calculo(numero1, numero2)


def get_operacao_usuario():
    return int(input('Informe qual operação gostaria de realizar: '))


if __name__ == '__main__':
    mensagem_operacoes()
    operacao = get_operacao_usuario()

    while not operacao_valida(operacao):
        print('Operação inválida')
        operacao = get_operacao_usuario()

    print(f'({nome_operacao(operacao).upper()})')
    numero1 = int(input('Informe o 1º número: '))
    numero2 = int(input('Informe o 2º número: '))
    resultado = efetua_operacao(operacao, numero1, numero2)
    print(f'O resultado da {nome_operacao(operacao)} é {resultado}')
