nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))
nota3 = float(input("Entre com a terceira nota: "))

faltas = int(input("Entre com o total de faltas: "))

limite = 25*80/100
if faltas > limite:
    print("Reprovação por falta" )
else:
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        print("Aprovado!")
    else:
        print("Reprovado!")