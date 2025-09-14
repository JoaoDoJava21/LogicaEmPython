import os 
os.system("cls || clear")

contador = 1 

while True:
    usuario = int(input("Digite o seu número: ")) 
    if usuario == 0:
        break
    contador += 1 


print("\nVocê digitou 0 o laço foi encerrado\n")
print("Quantas vezes o número foi digitado: " , contador , "\n")
