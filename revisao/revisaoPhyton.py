# 1. Variaveis e tipos de dados
# sao usadas para armezenar dados e realizar contas e ser alterado durante o codigo
# exemplo 1: criando uma variavel
x = 20

# Exemplo 2: mudando o valor
x = x + 1

# 2. Operadores 
# atribuição,aritmeticos,relacionais,logicos sao os tipos de operadores do phyton que servem basicamente para atribuir valores a variaveis
# exemplo:
'''
adiçao (+) (adiçao = x + y)
subtraçao (-) (subtrçao = x - y)
multiplicacao (*) (multplicaçao = x * y)
divisao normal (/) (divisao = x / y)
divisao inteira (//) (divisao inteira x // y)
resto (%) (resto x % y)
potenciaçao (**) (potencia x ** y)
'''

# 3.Entradas de dados
# em phyton, a entrada de dados é realizada atraves do input() essa funçao espera que o usuario digite um valor pelo teclado e pressione a tecla Enter para enviar a resposta
# exemplo:
nome = input("seu nome: ")
print("Olá, " + nome + "!")

# 4. saida de dados
# em phytom a saida de dados é realiizada através da função print, essa função recebe um ou mais argumentos que podem ser variaveis, valires constantes, strings e expressões, e exibe o resultado na saida padrão.
print("Ola mundo")  

# 5. Estrutura de repitição
#é um bloco que repete um comando sem parar ate que o usuario faca uma acao ou o usuario dita um tanto de repeticoes
ola = True 
while ola == True: 
    print("ola")

# 6. Estrutura de condição
# em phyton, as estruturas condicionais if, elfi e else sao utilizadas para executar diferentes blocos de codigo, dependendo do resultado de uma condição especifica.
num = int(input("digite um numero: "))
if num > 0:
    print("o numero é positivo.")
elif num < 0:
    print("o numero é negativo.")
else:
    print("o numero é zero")    

