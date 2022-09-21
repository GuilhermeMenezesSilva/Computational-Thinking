destino = input("Para onde deseja ir? ")

if destino == 'Norte':
    ida_volta = input('A viagem é somente ida ou ida e volta? ')
    if ida_volta == 'Ida':
        print('O preço da passagem é de R$280 reais')
    elif ida_volta == 'Ida e volta':
        print('O preço da passagem é de R$400 reais')
    else:
        print('Opção inválida')

elif destino == 'Nordeste':
    ida_volta = input('A viagem é somente ida ou ida e volta? ')
    if ida_volta == 'Ida':
        print('O preço da passagem é de R380 reais')
    elif ida_volta == 'Ida e volta':
        print('O preço da passagem é de R$628 reais')
    else:
        print('Opção inválida')

elif destino == 'Centro-Oeste':
    ida_volta = input('A viagem é somente de ida ou ida e volta? ')
    if ida_volta == 'Ida':
        print('O valor da passagem é de R$620 reais')
    elif ida_volta == 'Ida e volta':
        print('O valor da passagem é de R$1100 reis')
    else:
        print('Opção inválida')

else:
    print('Destino inexistente')