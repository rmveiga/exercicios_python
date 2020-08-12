def numero_par_ou_impar(numero):
    if numero % 2 == 0:
        return f'O número {numero} é par'
    return f'O número {numero} é impar'


numero = int(input('Informe um número inteiro qualquer: '))
print(numero_par_ou_impar(numero))
