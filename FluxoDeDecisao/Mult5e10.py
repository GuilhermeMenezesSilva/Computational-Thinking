num1 = int(input("Digite um numero: "))

if num1 % 5 == 0 and num1 % 10 == 0:
    print(f"O numero {num1} é multiplo de 5 e de 10 ao mesmo tempo")
else:
    print(f"O numero {num1} não é multiplo")