## Data: 30/06/2026
## Jogo: Par ou Ímpar
## Disciplina: PCAP
## Aluno: Benício Cordeiro

# Como jogar:

O jogador disputa partidas de Par ou Ímpar contra a máquina até que um dos dois complete 3 vitórias.

O jogador escolhe um número entre 0 e 5;
O jogador aposta se a soma será "par" ou "ímpar";
A máquina gera um número aleatório também de 0 a 5;
O vencedor da rodada é definido pela soma dos dois números.

# Regras do Jogo:

Se a soma dos dois números for divisível por 2, o resultado é PAR;
Caso contrário, o resultado é ÍMPAR;
Ganha a rodada quem acertou a aposta inicial (Jogador ou Máquina);
O jogo termina assim que um dos lados atingir 3 pontos.

# Pilares e Conceitos Utilizados

Funções
Utiliza as funções quem_venceu(), jogar() e main() para modularizar e organizar a lógica principal do jogo.

Estruturas Condicionais
Uso de if, elif e else para validar as entradas do usuário e para verificar se a soma é par ou ímpar.

Laços de Repetição
Uso do laço while True para validação de dados (garantir escolhas certas) e while jogador < 3 and maquina < 3 para controlar o fluxo do placar até o fim do jogo.

Random
Usa a biblioteca random para gerar o número secreto da máquina através do comando:

random.randint(0, 5)

Validação
Valida se o número digitado está entre 0 e 5, e se a string digitada corresponde a "par" ou "ímpar" (tratando também o caractere com acento "ímpar").

Variáveis
Controla o placar e o estado do jogo através das variáveis:
"jogador"
"maquina"
"soma"
"aposta"

# Parte criada por eu mesma

Criei uma lógica de tratamento de texto na linha 36 com .lower() e uma estrutura condicional nas linhas 38-39 para converter "ímpar" (com acento) em "impar" (sem acento), evitando que o programa quebre ou invalide a resposta correta do usuário por causa da acentuação.

##  Autoavaliação

Conceito pretendido: [C]

Justificativa (par_impar.py linhas 10-91):
O jogo funciona ............: par_impar.py, linha 10 a 91
Trabalho com texto .........: par_impar.py, linha 34 (.lower() e tratamento de acentuação)
Documentação e Git .........: README.md criado e commits realizados no GitHub
Extensão/originalidade .....: par_impar.py, linhas 38 a 39 Adaptação para aceitar a palavra digitada com ou sem acento gráfico