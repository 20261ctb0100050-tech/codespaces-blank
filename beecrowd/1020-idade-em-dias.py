'''
Problema: beecrowd | 1020
Data: 2026.05.14
Estudante: Gustavo Heitor Ribeiro
'''

# Objetivo: Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

# --- ANÁLISE (LIAC) ---
# Entrada: O arquivo de entrada contém um valor inteiro
# Processamento: // e % 
# Saída: Imprima a saída conforme exemplo fornecido

D = int(input())
# Recebe o número de dias

ano = D // 365
# a é a quantidade de anos que foi convertida de dias para anos

D = D % 365 
# Recebe quantos dias sobraram do ano

mes = D // 30
# Calcula os dias que sobraram em meses

dia = D % 30
# Mostra os dias que sobraram dos meses

print(f"{ano} ano(s)")
# Mostra anos

print(f"{mes} mes(es)")
# Mostra meses

print(f"{dia} dia(s)")
# Mostra dias