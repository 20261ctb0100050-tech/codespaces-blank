# =======================================
# Arquivo:      main.py
# Disciplina:   2026-PCAP
# Aula:         20
# Autor:        Gustavo Heitor ribeiro
# Data:         2026.08.04
# Conceitos:    Menu principal, gerenciamento de estado e fluxo do app
# =======================================

from telas import titulo, linha
from adivinhe import jogar_adivinhe
from ppt import jogar_ppt
from parimpar import jogar_parimpar
from jogodavelha import jogar_jogodavelha
from modulos import ler_opcao
from placar import salvar_placar, carregar_placar
from jogadores import menu_jogadores, salvar_jogadores, carregar_jogadores

NOME_DO_DONO = 'Gustavo'
NOMES_DOS_JOGOS = ['Adivinhe o Numero', 'Pedra-Papel-Tesoura', 'Par ou Impar', 'Jogo da Velha']

# Carregamento seguro dos dados do placar e jogadores
try:
    vezes_jogado = carregar_placar()
    # Se o placar não carregar como uma lista com os 3 jogos, cria uma lista padrão de zeros
    if not isinstance(vezes_jogado, list) or len(vezes_jogado) < 3:
        vezes_jogado = [0, 0, 0, 0]
except Exception:
    vezes_jogado = [0, 0, 0, 0]

try:
    jogadores = carregar_jogadores()
except Exception:
    jogadores = []


def mostrar_placar():
    titulo('PLACAR')
    for i in range(len(NOMES_DOS_JOGOS)):
        print(NOMES_DOS_JOGOS[i] + ': ' + str(vezes_jogado[i]) + 'x')
    linha()


while True:
    titulo('FLIPERAMA DO ' + NOME_DO_DONO)
    print('[5] - Jogadores')
    print('[4] - Jogodavelha ')
    print('[3] - Par ou Ímpar')
    print('[2] - Pedra - Papel - Tesoura')
    print('[1] - Jogo Adivinhe o Número')
    print('[0] - Sair do Fliperama')
    linha()

    opcao = ler_opcao('Escolha uma opção', ['0', '1', '2', '3', '4', '5'])

    if opcao == '0':
        mostrar_placar()
        salvar_placar(vezes_jogado)
        salvar_jogadores(jogadores)
        titulo('Ate a proxima!')
        break

    if opcao == '5':
        menu_jogadores(jogadores)
    else:
        # Ajusta o índice baseado na opção escolhida (1, 2 ou 3)
        indice = int(opcao) - 1
        vezes_jogado[indice] += 1

        if opcao == '1':
            jogar_adivinhe()
        elif opcao == '2':
            jogar_ppt()
        elif opcao == '3':
            jogar_parimpar()
        elif opcao == '4':
            jogar_jogodavelha()

        input('pressione enter para voltar ao menu...')