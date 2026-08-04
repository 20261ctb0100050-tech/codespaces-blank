# ==============================================================
# ARQUIVO:     telas.py  
# Disciplina: 2026-PCAP
# Aula:        20 
# Autor:       [Gustavo Ribeiro]
# Data:         2026.08.04
# Conceitos  : <o que este arquivo usa>
# ==============================================================

# Definicao da moldura caracteres e tamanho
CAR = '#'
TAM = 40

# Desenha uma linha na tela
def linha():
    print(CAR * TAM)

# Desenha um texto entre linhas 
def titulo(texto):
    linha()
    print(texto.center(TAM))
    linha()

