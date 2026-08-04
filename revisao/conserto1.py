# conserto 1: trecho do "adivinhe o numero" (Aula 16)
import random
print("=== ADIVINHE O NUMERO ===")
segredo = random.randint(1, 10)
palpite = int(input("digite um numero de 1 a 10: "))
if palpite == segredo:
    print("Acertou!")
else:
    print("Errou! O segredo era" , segredo)
