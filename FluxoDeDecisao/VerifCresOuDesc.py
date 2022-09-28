num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

if num1 < num2 and num2 < num3:
    print("Numeros digitados em ordem crescente")
else:
    print("Numeros digitados em ordem decrescente")