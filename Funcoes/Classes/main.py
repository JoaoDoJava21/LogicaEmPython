import os 
os.system("cls || clear")
from pessoa import Pessoa

p1 = Pessoa()
p2 = Pessoa()

p1.nome = "Luiz" # Atributos de instância
p2.nome = "João"

print(p1.nome) # Variáveis de Instancia
print(p2.nome)