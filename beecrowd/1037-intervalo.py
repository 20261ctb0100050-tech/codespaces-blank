'''
Problema: beecrowd 1037
Data: 23/04/26
Aluno: Gustavo Ribeiro 
''' 
# Objetivo: Ler um valor float e indicar em qual intervalo ele se enquadra

#--- ANALISE (LIAC) ---
# Entrada: um número de ponto flutuante qaulquer
#Processamento: verificar em qual dos intervalos o valor se enquadra
#   [0,25]      0 <= 25
#   (25,50)     25 < valor <= 50
#   (50,75)     50 < valor <= 75
#   (75,100)    75 < valor <= 100
#   fora       qualquer outro valor
# Saída: mensagem com intervalo correspondente ou "Fora de intervalo"

valor = float(input())

# Cada elif só é testado se todas as condições anteriores forem falsas
#Isso elimina a necessidade de ifs aninhados código mais limpo e legível
if 0 <= valor <= 25:
    # Colchete [ indica que o extremo está incluindo no intervalo
    print("Intervalo [0,25]")
elif 25 < valor <= 50:
    #Paréntese (indica que 25 não está incluído apenas valores maiores que 25
    print("Intervalo (25,50]")
elif 50 < valor <= 75:
    print("Intervalo (50,75]")
elif 75 < valor <= 100:
    print("Intervalo (75,100]")
else:
    # Nenhum intervalo correspondeu: valor negativa ou acima de 100
    print("Fora de intervalo")