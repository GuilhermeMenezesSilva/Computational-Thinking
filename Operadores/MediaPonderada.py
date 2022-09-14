n1 = int(input("Digite a primeira nota: "))
pesoN1 = int(input("Qual o peso dessa nota? "))
n2 = int(input("Digite a segunda nota: "))
pesoN2 = int(input("Qual o peso dessa nota? "))
n3 = int(input("Digite a terceira nota: "))
pesoN3 = int(input("Qual o peso dessa nota? "))

mediaPonderada = (pesoN1*n1 + pesoN2*n2 + pesoN3*n3) / (pesoN1 + pesoN2 + pesoN3)

print("A média ponderada desse aluno é", mediaPonderada)