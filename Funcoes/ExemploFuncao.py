import os 
os.system("cls || clear")


# Funcção para somar Valor A e B
def soma(a,b):
    return a + b

print(soma(5,10))

# Ou 

# a = int(input("Digite o valor de a: "))
# b = int(input("Digite o valor de b: "))

# print("Resultado da soma:", soma(a, b))

print("\n")

# Função para somar todos os valores que eu passar na minha lista 

def somarLista(lista):
    total = 0
    for n in lista:
        total += n 
    return total

print("Seu resultado: " , somarLista([10,20,30]))


# Função para dobrar o valor 

print("\nPara dobrar o número exemplo")

def dobrar(n):
    return n*2

print(dobrar(7))