'''
Problema: beecrowd | 1014
Data: 2026.04.16
Estudante: Gustavo Ribeiro
'''
# Objetivo: Calcular o consumo médio de um automóvel em km/l

# --- ANÁLISE (LIAC) ---
# Entrada: int X (inteiro, em km) e float Y (float, em litros)
# Processamento: consumo = x (km)/ y (L)
# Saída: consumo com 3 casas decimais seguido de (km/l)

# Lê a distância total percorrida em km (tipo inteiro)
X = int(input())

# Lê o total de combustível gasto em litros (tipo ponto flutuante)
Y = float(input())

# Calcula o consumo médio: quilômetro dividido por litros
consumo = X / Y

# Exibe o resultado com 3 casas decimais e a unidade km/l
print(f"{consumo:.3f} km/l")