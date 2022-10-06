numeros = []

for i in range(7):
    numeros.append(int(input("Entre com um número inteiro: ")))

print("--- Múltiplos de 2 ---")
for i in range(7):
    if numeros[i]%2==0: #multiplo de 2
        print(numeros[i])

print("\n--- Múltiplos de 3 ---")
for i in range(7):
    if numeros[i]%3==0: #multiplo de 3
        print(numeros[i])
