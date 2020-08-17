nome_completo = str(input('Informe o seu nome completo: '))
primeiro_nome = lambda nome: nome.split()[0]
ultimo_nome = lambda nome: nome.split()[-1]

print(f'Seu primeiro nome é {primeiro_nome(nome_completo)} '
      f'e o seu último nome é {ultimo_nome(nome_completo)}')