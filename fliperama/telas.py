# =======================================
# Arquivo:      telas.py
# Disciplina:   2026-PCAP
# Aula:         20
# Autor:        Gustavo Ribeiro
# Data:         2026.08.04
# Conceitos:    Molduras e títulos centralizados
# =======================================

CAR = '='
TAM = 40


def linha():
    print(CAR * TAM)


def titulo(texto):
    linha()
    print(texto.center(TAM))
    linha()