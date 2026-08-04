# ==============================================================
# ARQUIVO:     telas.py  
# Disciplina: 2026-PCAP
# Aula:        20 
# Autor:       [Gustavo Ribeiro]
# Data:         2026.08.04
# Conceitos  : <o que este arquivo usa>
# ==============================================================

# importar funçoes de arquivos (módulos)
from telas import titulo, linha
from adivinhe import jogar_adivinhe
from modulos import ler_opcao

titulo('FLIPERAMA DA PESSOA PASSARO')

while True:
    titulo('FLIPERAMA DO PESSOA PASSARO')
    print('1 - Jogo Adivinhe o Numero')
    print('0 - Sair do Fliperama')
    opcao = input('Escolha uma opção: ').strip()

    if opcao == '0':
        print('Até a Proxima!')
        break
    elif opcao == '1':
        jogar_adivinhe()  