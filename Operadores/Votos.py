Lula = int(input("Quantos votos Lula teve? "))
Bolsonaro = int(input("Quantos votos bolsonaro teve? "))
Ciro = int(input("Quantos votos ciro teve? "))
votoBranco = int(input("Quantos votos em branco teve? "))
votoNulo = int(input("Quantos votos nulos teve? "))

totalEleitores = Lula + Bolsonaro + Ciro + votoBranco + votoNulo

porcentualVotosLula = totalEleitores * (Lula/100)
porcentualVotosBolsonaro = totalEleitores * (Bolsonaro/100)
porcentualVotosCiro = totalEleitores * (Ciro/100)
porcentualVotosBranco = totalEleitores * (votoBranco/100)
porcentualVotosNulos = totalEleitores * (votoNulo/100)

print("O total de eleitores foi", totalEleitores)
print("O porcentual de votos do Lula foi", porcentualVotosLula)
print("O porcentual de votos do Bolsonaro foi", porcentualVotosBolsonaro)
print("O porcentual de votos do Ciro foi", porcentualVotosCiro)
print("O porcentual de votos em branco foi", porcentualVotosBranco)
print("O porcentual de votos nulos foi", porcentualVotosNulos)