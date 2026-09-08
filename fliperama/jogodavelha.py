# ===================================================================
# ARQUIVO   : jogodavelha.py (ou meujogo.py, conforme seu main.py)
# Autor     : Gustavo Heitor
# Data      : 2026.08.20
# Conceitos : Jogo da Velha contra Computador integrado ao Fliperama
# ===================================================================

import random
from telas import titulo, linha
from modulos import ler_numero # Importado para validar os inputs do usuário

def imprime_tabuleiro(tab):
    print("\n  0   1   2")
    for i, l in enumerate(tab):
        print(f"{i} " + " | ".join(l))
        if i < 2:
            print("  ---------")

def verifica_vitoria(tab, jogador):
    for i in range(3):
        if all(tab[i][j] == jogador for j in range(3)) or all(tab[j][i] == jogador for j in range(3)):
            return True
    if all(tab[i][i] == jogador for i in range(3)) or all(tab[i][2 - i] == jogador for i in range(3)):
            return True
    return False

def verifica_empate(tab):
    return all(tab[i][j] != ' ' for i in range(3) for j in range(3))

def jogada_computador(tab):
    posicoes_livres = [(r, c) for r in range(3) for c in range(3) if tab[r][c] == ' ']
    return random.choice(posicoes_livres)

# Nome da função alterado para bater com o import do seu main.py
def jogar_jogodavelha():
    # Inicializa o tabuleiro DENTRO da função para limpar a cada nova partida
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    
    humano = 'X'
    computador = 'O'
    jogador_atual = humano
    
    titulo('JOGO DA VELHA') # Uso do seu módulo de telas
    
    while True:
        imprime_tabuleiro(tabuleiro)
        
        if jogador_atual == humano:
            print("\nSua vez (X)!")
            
            # Substituição dos inputs com tratamento por ler_numero
            # Supondo que seu ler_numero aceite a mensagem e os limites válidos
            linha_escolhida = ler_numero("Escolha a linha (0, 1 ou 2): ", 0, 2)
            coluna_escolhida = ler_numero("Escolha a coluna (0, 1 ou 2): ", 0, 2)

            if tabuleiro[linha_escolhida][coluna_escolhida] != ' ':
                print("Essa posição já está ocupada! Tente novamente.")
                continue
                
            tabuleiro[linha_escolhida][coluna_escolhida] = humano
        else:
            print("\nO computador (O) está pensando...")
            l, c = jogada_computador(tabuleiro)
            tabuleiro[l][c] = computador
            print(f"O computador escolheu a linha {l} e coluna {c}.")
            linha()

        if verifica_vitoria(tabuleiro, jogador_atual):
            imprime_tabuleiro(tabuleiro)
            linha()
            if jogador_atual == humano:
                print("Parabéns! Você venceu o computador!")
            else:
                print("O computador venceu!")
            linha()
            break

        if verifica_empate(tabuleiro):
            imprime_tabuleiro(tabuleiro)
            linha()
            print("O jogo terminou em empate!")
            linha()
            break

        jogador_atual = computador if jogador_atual == humano else humano

if __name__ == "__main__":
    jogar_jogodavelha()
