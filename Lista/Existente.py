numeros = []

for i in range(15):
    numeros.append(int(input("Entre com um número inteiro: ")))

print("--- Posições dos números 30 ---")
for i in range(15):
    if numeros[i]==30:
        print(i)
