def troco (dinheiro, valor):
    diferença = (dinheiro - valor)
    notas5 = diferença // 5
    diferença = diferença - (notas5 * 5)
    notas2 = diferença // 2
    diferença = diferença - (notas2 * 2)
    moedas1 = diferença // 1
    diferença = diferença - (moedas1 * 1)
    moedas50 = diferença // 0.5
    diferença = diferença - (moedas50 * 0.5)
    moedas25 = diferença // 0.25
    diferença = diferença - (moedas25 * 0.25)
    moedas10 = diferença // 0.10
    diferença = diferença - (moedas10 * 0.10)
    moedas5 = diferença // 0.05
    diferença = diferença - (moedas5 * 0.05)
    moedas01 = diferença // 0.01
    diferença = diferença - (moedas01 * 0.01)
    diferença = round(diferença, 2)
    if diferença == 0.01:
        moedas01 = moedas01 + 1
    if notas5 > 0:
        print('Nota(s) de 5 R$: {}'.format(notas5))
    if notas2 > 0:
        print('Nota(s) de 2 R$: {}'.format(notas2))
    if moedas1 > 0:
        print('Moeda(s) de 1 R$: {}'.format(moedas1))
    if moedas50 > 0:
        print('Moeda(s) de 50 centavos: {}'.format(moedas50))
    if moedas25 > 0:
        print('Moeda(s) de 25 centavos: {}'.format(moedas25))
    if moedas10 > 0:
        print('Moeda(s) de 10 centavos: {}'.format(moedas10))
    if moedas5 > 0:
        print('Moeda(s) de 5 centavos: {}'.format(moedas5))
    if moedas01 > 0:
        print('Moeda(s) de 1 centavo: {}'.format(moedas01))
    return

estoque = [2,5,1,100,2]

while True:
    print('------------------------------------')
    codigo = int(input('ID |  Produto  |  Valor   | Estoque \n'
                    '1  | Coca Cola | R$ 3.75  | {} \n'
                    '2  |   Pepsi   | R$ 3.67  | {} \n'
                    '3  |  Monster  | R$ 9.96  | {} \n'
                    '4  |   Café    | R$ 1.25  | {} \n'
                    '5  |  Redbull  | R$ 13.99 | {} \n'
                    '------------------------------------\n'
                    'Por favor, escolha seu produto:'.format(estoque[0],estoque[1],estoque[2],estoque[3],estoque[4])))

    if codigo < 1 or codigo > 5:
        print('Produto Inválido, consulte a tabela.')
        continue

    elif codigo == 1:
        print('Preço: 3.75 R$')
        if estoque[0] == 0:
            print('Produto fora de estoque!')
            continue
        dinheiro = float(input('Entre com Saldo: '))
        while dinheiro < 3.75:
            print('Dinheiro Insuficiente!')
            dinheiro = float(input('Entre com Saldo: '))
        if dinheiro > 3.75:
            print('Seu Troco:')
            troco(dinheiro,3.75)
        estoque[0]-=1

    elif codigo == 2:
        print('Preço: 3.67 R$')
        if estoque[1] == 0:
            print('Produto fora de estoque!')
            continue
        dinheiro = float(input('Entre com Saldo: '))
        while dinheiro < 3.67:
            print('Dinheiro Insuficiente!')
            dinheiro = float(input('Entre com Saldo: '))
        if dinheiro > 3.67:
            print('Seu Troco:')
            troco(dinheiro,3.67)
        estoque[1] -= 1

    elif codigo == 3:
        print('Preço: 9.96 R$')
        if estoque[2] == 0:
            print('Produto fora de estoque!')
            continue
        dinheiro = float(input('Entre com Saldo: '))
        while dinheiro < 9.96:
            print('Dinheiro Insuficiente!')
            dinheiro = float(input('Entre com Saldo: '))
        if dinheiro > 9.96:
            print('Seu Troco:')
            troco(dinheiro,9.96)
        estoque[2] -= 1

    elif codigo == 4:
        print('Preço: 1.25 R$')
        if estoque[3] == 0:
            print('Produto fora de estoque!')
            continue
        dinheiro = float(input('Entre com Saldo: '))
        while dinheiro < 1.25:
            print('Dinheiro Insuficiente!')
            dinheiro = float(input('Entre com Saldo: '))
        if dinheiro > 1.25:
            print('Seu Troco:')
            troco(dinheiro,1.25)
        estoque[3] -= 1

    else:
        print('Preço: 13.99 R$')
        if estoque[4] == 0:
            print('Produto fora de estoque!')
            continue
        dinheiro = float(input('Entre com Saldo: '))
        while dinheiro < 13.99:
            print('Dinheiro Insuficiente!')
            dinheiro = float(input('Entre com Saldo: '))
        if dinheiro > 13.99:
            print('Seu Troco:')
            troco(dinheiro,13.99)
        estoque[4] -= 1






