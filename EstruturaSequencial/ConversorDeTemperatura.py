import os 
os.system("cls || clear")

# Entrada
celsius = float(input("Digite a temperatura em Celsius: "))

# Processamento
fahrenheit = (celsius * 9/5) + 32

# Saída
print(f"{celsius}°C equivalem a {fahrenheit}°F")