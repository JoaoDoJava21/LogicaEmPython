#Peça a idade e classifique em:
# Criança (0–12)
# Adolescente (13–17)
# Adulto (18–59)
#Idoso (60+)

print("Programa de Classificação de Idade\n")

idade = int(input("Digite a sua idade: "))

if idade <= 12:
    print("Você é criança")
elif idade <= 17:
    print("Você é adolescente")
elif idade <= 59:
    print("Você é Adulto")
else:
    print("Você é idoso")
