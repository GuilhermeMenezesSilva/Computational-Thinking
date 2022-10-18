frase = input("Digite uma frase: ")
print(frase)

def qtdFrase(frase):
    frase = frase.lower() #Transforma a frase em minuscula
    frase = frase.replace(",",'') #Tira a virgula
    frase = frase.replace(".",'') #Tira os pontos finais
    frase = frase.split(" ") #Separa as strings
    print(frase)
    dic = {}
    for palavra in frase:
        if palavra not in dic.keys():
            dic[palavra] = 1
        else:
            dic[palavra]+=1
    return dic
print(qtdFrase(frase))