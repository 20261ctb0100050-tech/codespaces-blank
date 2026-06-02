'''
Problema: beecrowd | 1006
Data: 07/05/2026
Estudante: Gustavo Ribeiro
'''

# Objetivo: Ler duas notas com pesos diferentes e calcular a média ponderada

# --- ANÁLISE (LIAC) ---
# Entrada: notas de ponto flutuante A, B e C (cada uma em uma linha)
# Processamento: média ponderada = (A * 2 + B * 3 + C * 5.0) / 10
# Saída: exibir no formato exato "MEDIA = valor" com 5 casas decimais

# float(input()) -> notas podem ter casas decimais
A = float(input())
B = float(input())
C = float(input())

# Nota A tem peso 2 e nota B tem peso 3 Nota C tem 5 de peso
# A soma dos pesos é 10 - divide-se por 10 para obter a média ponderada
MEDIA = (A * 2 + B * 3 + C * 5.0) / 10

# :.1f dentro da f-string -> formata o número com exatamente 1 casas decimais
# O enunciado exige espaço antes e depois do = - seguir à risca
print(f"MEDIA = {MEDIA:.1f}")