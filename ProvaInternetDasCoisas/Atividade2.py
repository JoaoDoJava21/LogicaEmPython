import os
os.system("cls || clear")

# Pede as três notas ao usuário e converte para números de ponto flutuante (float)
nota1 = float(input("Digite a nota da 1ª unidade: "))
nota2 = float(input("Digite a nota da 2ª unidade: "))
nota3 = float(input("Digite a nota da 3ª unidade: "))


media = (nota1 + nota2 + nota3) / 3

# Exibe a média final formatada
print(f"\nSua média final é: {media:.1f}")


if media >= 7:
    print("Situação: APROVADO! ")
elif media >= 5: 
    print("Situação: RECUPERAÇÃO! ")
else:
    print("Situação: REPROVADO! ")