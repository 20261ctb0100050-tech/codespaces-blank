# ===================================================================
# ARQUIVO   : parimpar.py (pasta fliperama)
# Autor     : Gustavo Ribeiro
# Data      : 2026.08.04
# Conceitos : Operador módulo (%), tomada de decisão e números aleatórios
# ===================================================================

from random import randint
from telas import titulo, linha
from modulos import ler_opcao, ler_numero


def jogar_parimpar():
    titulo('JOGO PAR OU ÍMPAR')

    escolha = ler_opcao('Você quer Par ou Ímpar? [P/I]', ['P', 'I', 'p', 'i']).upper()
    num_jogador = ler_numero('Digite um número entre 0 e 10', 0, 10)
    num_computador = randint(0, 10)

    soma = num_jogador + num_computador
    resultado = 'P' if soma % 2 == 0 else 'I'

    print(f'Você jogou {num_jogador} e o computador jogou {num_computador}. Total: {soma}')
    print('Deu PAR!' if resultado == 'P' else 'Deu ÍMPAR!')

    if escolha == resultado:
        print('Parabéns, você VENCEU!')
    else:
        print('Que pena, você PERDEU!')

    linha()