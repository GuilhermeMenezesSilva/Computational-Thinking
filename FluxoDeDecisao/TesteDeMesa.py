# Faça o teste de mesa para numero_1= 15 e numero_2= 6
numero_1 = int(15)
numero_2 = int(6)
resultado = ((numero_1%2)*3)+(13-2+numero_2)

# Responda: 
# a) Qual o conteúdo da variável resultado quando termina o algoritmo?
print(resultado)

# b) Analise o pseudocódigo e responda: o que mostrará na tela?
print("Resultado maior que zero e menor ou igual a 20")

# c) Reescrever o algoritmo utilizando a linguagem de programação Python.
numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite um numero: "))

resultado = ((numero1%2)*3)+(13-2+numero2)

if resultado <= 0: 
    print("Resultado menor ou igual a zero")
else:
    if resultado > 0 and resultado <= 20:
        print("Resultado maior que zero e menor ou igual a 20")
    else:
        print("resultado maior que 20")