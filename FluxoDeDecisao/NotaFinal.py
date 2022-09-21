trLab   =   int(input('Digite a nota do trabalho de laboratorio: '))
avSem   =   int(input('Qual a nota da avaliação semestral? '))
exFinal =   int(input('Digite a nota final do aluno: '))

mediaPonderada = 2*trLab + 3*avSem + 5*exFinal / (2+3+5)

if mediaPonderada >= 8:
    print('Conceito A')
elif mediaPonderada >= 7 or mediaPonderada == 7.9:
    print('Conceito B')
elif mediaPonderada >= 6 or mediaPonderada == 6.9:
    print('Conceito C')
elif mediaPonderada >= 5 or mediaPonderada == 5.9:
    print('Conceito D')
elif mediaPonderada <= 4.9 or mediaPonderada == 0:
    print('Conceito E')