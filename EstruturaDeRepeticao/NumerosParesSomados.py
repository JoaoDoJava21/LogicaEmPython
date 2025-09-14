# Some todos os números pares de 1 a 50 usando

contador = 1

opcao = input("Você deseja exibir números pares ou ímpares? ")

while contador <= 50:
    if opcao == "pares" and contador % 2 == 0:
        print(contador)
    if opcao == "impares" and contador % 2 != 0:
        print(contador)
    contador += 1
    
