# ════════════════════════════════════════════════════════════
# Disciplina : Pensamento Computacional, Algoritmos e Programação (PCAP)
# Projeto    : Jogo "Par ou Ímpar" 
# Arquivo    : par_impar_v2.py
# Autor      : Gustavo Heitor Ribeiro
# Data       : 30/06/2026
# ════════════════════════════════════════════════════════════
import random

def jogar():
    maquina = random.randint(0, 5)
    
    # Validação do número com tratamento de erro (caso digitem letras)
    while True:
        try:
            jogador = int(input("Escolha um número (0-5): "))
            if 0 <= jogador <= 5:
                break
            print("Número fora do intervalo permitido!")
        except ValueError:
            print("Entrada inválida!")
        
    # Validação da aposta simplificada com operador 'in'
    while True:
        aposta = input("Par ou Ímpar? ").strip().lower().replace("ímpar", "impar")
        if aposta in ["par", "impar"]:
            break
        print(" Digite apenas 'par' ou 'ímpar'.")
        
    soma = jogador + maquina
    # Lógica de vitória simplificada em uma linha (Expressão Condicional)
    resultado = "par" if soma % 2 == 0 else "impar"
    vencedor = "Jogador" if resultado == aposta else "Máquina"
    
    # Exibição limpa dos resultados da rodada
    print(f"\n Você colocou {jogador} e a Máquina {maquina} (Soma = {soma} -> {resultado.upper()})")
    print(f" Vencedor da rodada: {vencedor}\n" + "─" * 40)
    
    return vencedor

def main():
    placar = {"Jogador": 0, "Máquina": 0}
    print("====== INÍCIO DO JOGO: MELHOR DE 3 ======")
    
    # O jogo roda enquanto ninguém atingir 3 pontos
    while max(placar.values()) < 3:
        vencedor_rodada = jogar()
        placar[vencedor_rodada] += 1
        print(f"PLACAR: Jogador {placar['Jogador']} x {placar['Máquina']} Máquina\n")
        
    # Determina o campeão baseado em quem fez 3 pontos primeiro
    campeao = max(placar, key=placar.get)
    print(f" FIM DE JOGO! O grande vencedor foi: {campeao.upper()}!")

if __name__ == "__main__":
    main()
