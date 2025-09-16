import os
os.system("cls || clear")

def calcular_preco_passagem(distancia_km):
    """
    calcula o preço da passagem com base na distância
    R$ 0,50/km para viagens de até 200 km
    
    R$ 0,45/km para viagens mais longas
    
    """
    
    if distancia_km <= 200:
    
        preco = distancia_km * 0.50
    
    else:
    
        preco = distancia_km * 0.45
    return preco


# pede a distância ao usuário e converte para número
distancia = float(input("Digite a distância da viagem em km: "))


valor_final = calcular_preco_passagem(distancia)


print(f"\nO preço da sua passagem será de R$ {valor_final:.2f}")