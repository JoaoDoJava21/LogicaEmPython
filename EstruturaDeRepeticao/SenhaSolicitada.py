import os 
os.system("cls || clear")

contador = 1 

while True:
    usuario = int(input("Digite a sua senha: "))
    if usuario == 1234:
        print("Senha Correta. Bem vindo !")
        break
    else:
        print("Senha incorreta. Digite novamente !")
        continue