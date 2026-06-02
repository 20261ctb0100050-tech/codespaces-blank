'''
Problema: beecrowd | 1002
Data: 10/04/2026
Estudante: Gustavo Ribeiro
'''

# Objetivo: Calcular a área de um círculo e exibir com 4 casas decimais.

# --- ANÁLISE (LIAC) ---
# Entrada: Um valor de ponto flutuante (raio).
# Processamento: Calcular a área usando AREA = 3.14159 * raio^2.
# Saída: A mensagem "A=" seguida pelo valor da área com 4 casas decimais.

# Leitura do raio como número decimal
R = float(input())

# Defina pi conforme o enunciado indica
pi = 3.14159

# Qual é a fórmula da área do círculo?
AREA = pi * (R ** 2)

# Saída - observe o formato exato e o número de casas decimais no enunciado
print(f"A={AREA:.4f}")