# Data: 22/06/2026
# Jogo: Pedra-Papel-Tesoura
# Disciplina: PCAP
# Aluno: Gustavo Ribeiro

# Como jogar:

O jogador disputa uma partida de 5 rodadas contra uma IA. O jogador digita sua escolha entre pedra, papel ou tesoura; a máquina faz uma escolha aleatória; o vencedor de cada rodada é determinado pelas regras clássicas.
Regras do Jogo:

Pedra vence Tesoura; Tesoura vence Papel; Papel vence Pedra; Escolhas iguais resultam em empate.

# Pilares e Conceitos Utilizados
Funções — utiliza a função resultado() para encapsular e organizar toda a lógica de decisão do jogo.
Estruturas Condicionais — uso de if, elif e else dentro da função resultado() para comparar as jogadas e determinar o vencedor de cada rodada.
Laços de Repetição — uso do for para controlar as 5 rodadas da partida, e do while para permitir repetição do jogo.
Listas — armazenamento das opções válidas:

opcoes = ["pedra", "papel", "tesoura"]
Random — uso do random para gerar a escolha aleatória da máquina:

random.choice(opcoes)
Validação — verifica se a entrada do jogador é válida (if jogada_jogador not in opcoes), penalizando com ponto para a máquina em caso de entrada inválida.
Variáveis — controle do placar ao longo das rodadas através das variáveis:

pontos_jogador e pontos_maquina
Parte criada por mim mesmo

Criei uma opção para jogar novamente usando um laço while e uma variável play_again, controlada por uma entrada do jogador ao final de cada partida (digitando 1 para sim ou 2 para não).

# 🎯 Autoavaliação

Conceito pretendido: [B]
Justificativa:

O jogo funciona ............: ppt.py, linhas 11 a 53

Trabalho com texto .........: ppt.py, linha 33 (.lower().strip())

Documentação e Git .........: README.md criado e commits realizados no GitHub

Extensão/originalidade .....: ppt.py, linhas 24 a 26 — adaptação para permitir jogar novamente com while e variável play_again