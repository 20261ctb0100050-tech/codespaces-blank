'''
Problema: beecrowd | 1011
Data: 09/04/2026
Estudante: Gustavo 
'''
# Objetivo: Ler o raio de uma esfera e caucular seu volume com a formula (3/4) * pi * R³

# ---ANÁLISE (LIAC) ---
# Entrada: um número de ponto flutuante (o raio R)
# Processamento: aplicar a fórmola do volume da esfera
# Saída: exibir no formato "VOLUME = valor" com 3 casas decimais

# float()  corvente o  valor lido para número decimal (ponto flutuante)
R = float(input())

# O anunciado pede para atribuir pi como constante - não usar math.pi
pi = 3.14159

# 4.0/3 garante divisão decimal (não inteira) - conforme dica do enunciado
# R** R  elevado à terceira potêNCIA (R³)
V = (4.0 / 3) * pi * R ** 3 

# :.3f  formata o número com exatamente 3 casas decimais 
print(f"VOLUME = {V:.3f}")