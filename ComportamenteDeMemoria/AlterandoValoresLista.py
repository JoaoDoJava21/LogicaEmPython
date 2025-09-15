"""

Métodos úteis: 
    append , insert , pop , del , clear, extend + 
    Create Read Update Delete = lista[i] CRUD

"""
import os 
os.system("cls || clear")

lista = [10,20,30,40]
lista[2] = 300 # Alterar o valor para 300 
print("Alterei o valor da lista[2] para: " , lista[2])


lista.append(50) # Acrescenta um valor na lista
print("Lista com novo valor: " , lista)
ultimo_valor = lista.pop() # Remove o último valor da minha lista
print("O ultimo valor foi removido !" , lista , "Valor removido: " , ultimo_valor)

print("\nSegunda Lista")
lista2 = ["João Victor" , "Maria" , "Daniel" , 145]
del lista2[2] # Remove um item da minha lista

print("\n" , lista2)

print("\nSeguindo a Lista 2 ")

lista2.insert(0 , "Caio") # Acrescenta um valor na Lista
print(lista2 , " O valor que foi acrescentado: " , lista2[0])

lista2.insert(100,50000) # O valor do Insert sempre vai acrescentado no ultimo valor Ok deveria gerar Erro
# Levando em consideração para acessar-lo é sempre conta a lista e acessar o ultimo valor
print("Valor do Insert: " , lista2[4])
# lista2.clear() --> Esse comando Limpa a lista completa
print(lista2)

# inverter = lista[::-1]

# Ou 

# lista.reverse() 
print("\n")

lista_a = [1,2,3]
lista_b = [4,5,6]
# lista_c = lista_a + lista_b
lista_a.extend(lista_b) # Junta os valores da lista 
print(lista_a)
