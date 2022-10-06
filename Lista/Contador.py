numeros = []
soma = 0
negativos = 0

for i in range(10):
    numeros.append(float(input(f"Digite o valor para a posição {i}: ")))
    if numeros[i] < 0:
        negativos += 1
    else:
        soma += numeros[i]

print("Quantidade de números negativos: ", negativos)
print("Soma dos números positivos: ", soma)
