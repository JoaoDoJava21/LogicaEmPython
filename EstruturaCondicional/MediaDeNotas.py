import os 
os.system("cls || clear")


nota = float(input("Digite a sua nota: "))

if nota >= 7 :
    print("Você passou ! ")
elif nota < 7 and nota >= 5:
      print("Você está de recuperação !")
else:
    print("Você foi reprovado !")