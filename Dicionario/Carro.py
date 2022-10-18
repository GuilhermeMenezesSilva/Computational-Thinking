car = {"carro": [], "ano": []}
car["preço"] = []

for i in range(5):
    carro = input("Digite o carro que deseja: ")
    car["carro"].append(carro)
    fabricacao = int(input("Digite o ano de fabricação: "))
    car["ano"].append(fabricacao)
    npreco = float(input("Digite o preço do carro: "))
    car["preço"].append(npreco)
    print(car)

def menor_preco():
    menor_valor = car["preço"][0]
    for i in range (len(car["preço"])):
        if i < menor_valor:
            menor_valor = car["preço"][i]
            indice = i
            print(f'O menor valor é {car["carro"] [indice]} fabricado em {car["ano"][indice]} que vale R${menor_valor} reais')
    return 
menor_preco()

def maior_preco():
    maior_valor = car["preço"][0]
    for j in range (len(car["preço"])):
        if j > maior_valor:
            maior_valor = car["preço"][i]
            indice = j
            print(f'O menor valor é {car["carro"] [indice]} fabricado em {car["ano"] [indice]} que vale R${maior_valor} reais')
    return 
maior_preco()