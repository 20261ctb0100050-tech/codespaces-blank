# ==============================================================
# ARQUIVO:     telas.py  
# Disciplina: 2026-PCAP
# Aula:        20 
# Autor:       [Gustavo Ribeiro]
# Data:         2026.08.04
# Conceitos  : <o que este arquivo usa>
# ==============================================================

# importar bibliotecas e funçoes de arquivos (módulos)
from random import randint 
from telas import titulo, linha
from modulos import ler_numero

def jogar_adivinhe():
    titulo('JOGO ADIVINHE O NUMERO')
    print('tente adivinhar o numero que estou pensando entre 1 e 10.')
    segredo = randint(1, 10)
    tentativas = 0
    acertou = False

    while not acertou:
        palpite = ler_numero('Digite seu palpite', 1, 10)
        tentativas += 1

        if palpite < segredo:
            print('O numero secreto é maior. tente novamente.')
        elif palpite > segredo:
            print("O numero secreto é menor. Tente novamente")
        else:
            acertou = True
    else:
        print(f"Parabéns! Você acertou o número secreto {segredo} em {tentativas}")
        linha()