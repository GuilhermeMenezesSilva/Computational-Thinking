numero1 = int(input("Entre com o primeiro número: "))
numero2 = int(input("Entre com o segundo número: "))
soma = 0

if numero1 > numero2:
    aux = numero1
    numero1 = numero2
    numero2 = aux
for cont in range(numero1+1,numero2):
    soma+=cont
    
print("Soma dos elementos existentes: ",soma)