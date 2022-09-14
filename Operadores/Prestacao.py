valorBoleto = float(input("Qual o valor do boleto? "))
juros = float(input("Qual será o juros cobrado? "))
diasAtrasados = int(input("Quantos dias esta em atraso? "))

valorBoletoAtualizado = valorBoleto + (valorBoleto * (juros/100)) * diasAtrasados

print("O valor do boleto após a data de vencimento é ", valorBoletoAtualizado)