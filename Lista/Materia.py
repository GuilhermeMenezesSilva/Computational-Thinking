ctp_lista = []
ddd_lista = []
ambos_lista = []

continuar = True
print("Alunos que cursam a disciplina CTP - Computational Thinking using Python")
while continuar:
    ctp_lista.append(input("Entre com a matrícula: "))
    continuar = input("Digite <S> para continuar ").upper()
    if continuar != "S":
        break

continuar = True
print("Alunos que cursam a disciplina DDD - Domain Driven Design")
while continuar:
    ddd_lista.append(input("Entre com a matrícula: "))
    continuar = input("Digite <S> para continuar ").upper()
    if continuar != "S":
        break

for i in range(len(ctp_lista)):
    if ctp_lista[i] in ddd_lista:
        ambos_lista.append(ctp_lista[i])

print("Alunos que cursam simultaneamente as disciplinas CTP e DDD")

for matricula in ambos_lista:
    print(matricula)
