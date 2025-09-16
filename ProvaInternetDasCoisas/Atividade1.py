import os
os.system("cls || clear")

# velocidade ao usuário e converte para um número inteiro
velocidade = int(input("Digite a velocidade do carro (em km/h): "))

if velocidade > 80:
    print("\nVOCÊ FOI MULTADO! O limite de 80 km/h foi excedido.")
    
    km_acima = velocidade - 80
    multa = km_acima * 5.00
    
    print(f"O valor da multa é de R$ {multa:.2f}")
else:
    print("\nVelocidade dentro do limite permitido. Boa viagem!")