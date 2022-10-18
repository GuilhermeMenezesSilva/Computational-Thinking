def mercado ():
    mercadinho = {"Arroz": 18.99, "Feijão": 7.69, "Picanha": 59.99}
    print("O senhor pode estar comprando: Arroz, Feijão e Picanha")
    qtdCompra = int(input("Quantos itens deseja comprar? "))
    valor = []
    valorTotal = 0
    for i in range(qtdCompra):
        item = input("Qual item deseja comprar? ")
        valor.append(mercadinho[item])
        valorTotal = sum(valor)
        print(f"O valor total a ser pago é de R${valorTotal} reais")
    return
mercado()