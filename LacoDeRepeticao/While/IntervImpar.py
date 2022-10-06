num1 = int(input("Digite 1 número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
cont = 0

if num1 > num2:
    num1,num2 = num2,num1
while num1 < num2:
    num1 += 1
    if num1 % 2 != 0:
        cont+=1
        
print("Quantidade de ímpares: ",cont)