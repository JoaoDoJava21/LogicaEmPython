import random
import os  
os.system("cls || clear")

numero_da_sorte = random.randint(1,100)

tentativas = 0 

print("----- JOGO DA ADIVINHAÇÃO V2.1 -----")

while True:
    numero = int(input("\nDigite o número secreto: "))
    tentativas += 1
    os.system("clear")
    if  numero == numero_da_sorte :
        print(f"Você acretou o Numero da sorte em {tentativas} tentativas")
        break
    elif(numero > numero_da_sorte  ):
        print(f"Numero secreto é menor - Já gastou {tentativas} tentativas")
    else:
        print(f"Numero secreto é maior - Já gastou {tentativas} tentativas")
    

