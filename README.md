# Exercícios Python
Este repositório tem como objetivo reunir alguns exercícios para os interessados em estudar e reforçar seus conhecimentos na linguagem Python. Todos os exercícios contam com um enunciado e com uma solução proposta, porém cada pessoa pode implementar a solução da maneira que achar mais interessante.

Os exercícios foram divididos em dois níveis: **básico** e **avançado**. Mesmo que o seu nível de conhecimento na linguagem seja bem raso, ainda assim você encontrará desafios que seja capaz de concluir. Dentro de cada nível, existem diversas categorias de exercícios para você praticar seus conhecimentos.

Neste repositório, você também encontrará algumas sugestões de projetos onde você deve unir todos os conhecimentos adquiridos com os exercícios.

## Antes de começar
Confira algumas dicas antes que você dê o primeiro passo na sua jornada:
- Leia atentamente o enunciado (a solução pode estar nele);
- Não olhe a solução antes de tentar (exercite a sua lógica e criatividade);
- Não copie código (digitar é mais eficiente para o aprendizado do que Ctrl + C e Ctrl + V);
- Não perca demasiado tempo em um desafio só (ficar andando em círculos não vai te ensinar nada).

### Índice
- [Básico](#básico)<br>
  - [Funções](#funções)
  - [Listas](#listas)
  - [Mensagens](#mensagens)
  - [Números](#números)
  - [Strings](#strings)
- [Avançado](#avançado)
  - [Lambda](#lambda)
  - [Map](#map)
- [Projetos](#projetos)
  - [Jogos](#jogos)


## Básico
### Funções
1. Desenvolva um programa que tenha uma função que verifique se um número inteiro qualquer é par ou impar<br>
[Solução proposta 1](https://github.com/rmveiga/exercicios_python/blob/master/basico/functions/ex001/main.py)<br>
[Solução proposta 2](https://github.com/rmveiga/exercicios_python/blob/master/basico/functions/ex001/main2.py)

🔼[Voltar ao índice](#índice)🔼

### Listas
1. Desenvolva um programa que armazene quatro notas em uma lista e que apresente: a média final, a maior nota e a menor nota<br>
[Solução proposta](https://github.com/rmveiga/exercicios_python/blob/master/basico/listas/ex001/main.py)

🔼[Voltar ao índice](#índice)🔼

### Mensagens
1. Desenvolva um programa que apresente na tela a seguinte mensagem: **Hello World**<br>
[Solução proposta](https://github.com/rmveiga/exercicios_python/blob/master/basico/mensagens/ex001/main.py)

2. Desenvolva um programa que pergunte o seu nome e, ao teclar Enter, apresente uma saudação personalizada<br>
[Solução proposta](https://github.com/rmveiga/exercicios_python/blob/master/basico/mensagens/ex002/main.py)

🔼[Voltar ao índice](#índice)🔼

### Números
1. Desenvolva um programa que leia um número inteiro qualquer e que apresete o número informado, seguido do seu antecessor e do seu sucessor<br>
[Solução proposta](https://github.com/rmveiga/exercicios_python/blob/master/basico/numeros/ex001/main.py)

2. Desenvolva um programa que leia um número inteiro qualquer e que apresente o número informado com duas casas decimais<br>
[Solução proposta](https://github.com/rmveiga/exercicios_python/blob/master/basico/numeros/ex002/main.py)

3. Desenvolva um programa que leia quatro notas e que apresente a média final<br>
[Solução proposta](https://github.com/rmveiga/exercicios_python/blob/master/basico/numeros/ex003/main.py)

4. Desenvolva um programa que leia um número inteiro qualquer e que informe se este número é par ou impar<br>
[Solução proposta](https://github.com/rmveiga/exercicios_python/blob/master/basico/numeros/ex004/main.py)

🔼[Voltar ao índice](#índice)🔼

### Strings
1. Desenvolva um programa que altere em tempo de execução a palavra **Java** pela palavra **Python** na frase **Exercícios de Java**<br>
[Solução proposta](https://github.com/rmveiga/exercicios_python/blob/master/basico/strings/ex001/main.py)

🔼[Voltar ao índice](#índice)🔼

## Avançado
### Lambda
1. Desenvolva um programa que leia o seu nome completo e que apresente somente o seu primeiro e último nomes<br>
[Solução proposta](https://github.com/rmveiga/exercicios_python/blob/master/avancado/lambda/ex001/main.py)<br>

2. Desenvolva um programa que leia um número qualquer e informe se ele é par ou ímpar<br>
[Solução proposta](https://github.com/rmveiga/exercicios_python/blob/master/avancado/lambda/ex002/main.py)<br>

3. Desenvolva uma calculadora rudimentar onde o usuário deve informar: qual operação ele deseja realizar, quais os valores para a realização do cálculo (apenas dois valores) e o resultado da operação<br>
[Solução proposta](https://github.com/rmveiga/exercicios_python/blob/master/avancado/lambda/ex003/main.py)<br>

🔼[Voltar ao índice](#índice)🔼

### Map
1. Desenvolva um programa que converta todas as temperaturas desta lista em Celsius ([22.5, 40, 13, 29, 34]) para Fahrenheit<br>
[Solução proposta](https://github.com/rmveiga/exercicios_python/blob/master/avancado/map/ex001/main.py)<br>

🔼[Voltar ao índice](#índice)🔼

## Projetos

### Jogos
1. Desenvolva um jogo de acerte o número, onde o computador escolhe um número inteiro aleatório de 0 a 10, e o usuário tem 5 tentativas para adivinhar o número<br>
**OBS.: O design da tela pode ser implementado livremente**<br>
- **(PLUS)**: Implemente um sistema de pontuação com o seguinte comportamento: se o usuário adivinhar o número na primeira tentativa, receberá a pontuação máxima (ex. 100 pontos); se o usuário adivinhar o número na última tentativa, receberá a pontuação mínima (ex. 10 pontos); se o usuário não acertar o número, não receberá nenhum ponto.<br>
- **(PLUS)**: Implemente um controle de erros. Caso o jogador digite um número fora da faixa permitida ou caracteres não numéricos, o sistema deve notificar o jogador e solicitar o input correto.<br>
- **(PLUS)**: Implemente a opção de o usuário iniciar uma nova partida. Ao finalizar uma rodada, após o resultado final, o jogo deve perguntar se o jogador quer iniciar uma nova partida e, em caso negativo, encerrar a aplicação.<br>

[Solução proposta](https://github.com/rmveiga/exercicios_python/blob/master/projetos/jogos/ex001/main.py)<br>

🔼[Voltar ao índice](#índice)🔼
