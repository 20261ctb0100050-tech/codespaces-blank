'''
Problema: beecrowd | 1035
Data: 2026.05.14
Estudante: Gustavo Heitor Ribeiro
'''

# Objetivo: Leia 4 valores inteiros A, B, C e D, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos"

# --- ANÁLISE (LIAC) ---
# Entrada: Quatro números inteiros A, B, C e D
# Processamento: 
# Saída: Mostre a respectiva mensagem após a validação dos valores

A, B, C, D = map(int, input().split())
if (B > C) and (D > C) and (C + D > A + B) and (C > 0) and (D > 0) and (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")