soma = 0
qtde = 50

for cont in range(0,qtde):
    print("Entre com a {}a. idade".format(cont + 1))
    idade = int(input("--> "))
while idade < 0:
    print("Idade inválida. Digite novamente a {}a. idade".format(cont+1))
    idade = int(input("--> "))
soma += idade

print("Média: ",soma/qtde)
