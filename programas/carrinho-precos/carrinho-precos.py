itens = []
precos = []
total = 0


menu = int(input('Quantos itens no seu carrinho de compras? \n'))

for i in range(menu):
    item = input('Digite o item:\n')
    preco = float(input('Digite o preço:\n'))

    itens.append(item)
    precos.append(preco)

print('\nCalculando seu total...\n')

for i in precos:
    total += i

for i in range(len(itens)):
    print(itens[i] + ':', precos[i])

print(f'\nSeu total é: {total}')