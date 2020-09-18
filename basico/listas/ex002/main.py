notas = []
contador = 1

while contador < 5:
    notas.append(int(input(f'Informe a {contador}ª nota: ')))
    contador += 1

media = sum(notas) / len(notas)
print(f'Sua média final foi {media}')
if media >= 7:
    print('APROVADO')
else:
    notas.append(int(input('Informe a nota da prova final: ')))

    media = sum(notas) / len(notas)
    print(f'Sua média final foi {media}')
    if media >= 5:
        print('APROVADO')
    else:
        print('REPROVADO')