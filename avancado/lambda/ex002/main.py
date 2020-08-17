numero = int(input('Informe um número qualquer: '))
eh_par = lambda numero: numero % 2 == 0

if eh_par(numero):
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é impar')
