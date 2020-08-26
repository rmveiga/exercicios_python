numeros = [21, 5, 34, 8, 16, 7, 3]
soma_pares = sum(map(lambda n: n if n % 2 == 0 else 0, numeros))
soma_impares = sum(map(lambda n: n if n % 2 != 0 else 0, numeros))
print(f'A soma dos valores pares é {soma_pares} e dos ímpares é {soma_impares}')
