'''
Problema: beecrowd | 1044
Data: 2026.04.16
Estudante: Gustavo Ribeiro
'''
# Objetivo: Vetificar se dois inteiros são múltipols entre si

# --- ANÁLISE (LIAC) ---
# Processamento: identificar A e B na mesma linha separados por espaço
# Saída: "Sao Multiplos" "Nao sao Multiplos"

A,B = input().split()
A = int(A)
B = int(B)
 
# identifica maior e menor para aplicar o operador % corretamente
# (o resto sempre deve ser cauculado divindo o maior pelo menor)
if A > B:
      maior = A
      menor = B
else:
      maior = B
      menor = A
# Operador % (módulo): retorna o resto da divisão inteira
# Se o resto for
if maior % menor == 0:
      print("Sao Multiplos")
else:
      print("Nao sao Multiplos")      