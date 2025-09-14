# Calculadora simples

print("Digite um operador e dois números para fazer sua operação: \n")

operador = input("Digite o operador : ")

numero1 = int(input("Digite o seu primeiro número: "))
numero2 = int(input("Digite o seu segundo número: "))


if operador == "+":
    print(f"A soma dos seus números são de : {numero1 + numero2}")
elif operador == "-":
    print(f"A subtração dos seus números são de : {numero1 - numero2}")
elif operador == "*":
    print(f"A multiplicação dos seus números são de : {numero1 * numero2}")
elif operador == "/":
    print(f"A divisão dos seus números são de : {numero1 / numero2}")
else:
    print("Digite novamente um operador entre + , - , * , / ")
