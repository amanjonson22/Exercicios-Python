#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def soma_imposto(*,taxa_imposto, custo):
    taxa_imposto = taxa_imposto/100
    valor_com_imposto = custo*taxa_imposto
    custo_com_imposto = custo + valor_com_imposto
    return custo_com_imposto

quantidade_testes = int(input('Quantos preços você quer calcular? '))
imposto_fixo_mutavel = input('''\nO imposto é fixo[F] ou muda[M]?
=> ''').lower()
if imposto_fixo_mutavel == 'f':
    imposto = int(input('Imposto atual: '))
    for teste in range(quantidade_testes):
        preco = float(input('Preço do item: '))

        print(f'O item de preço R${preco:.2f} somado à {imposto}% de imposto é {soma_imposto(taxa_imposto= imposto, custo= preco):.2f}')
elif imposto_fixo_mutavel == 'm':
    for teste in range(quantidade_testes):
        imposto = int(input('Imposto atual: '))
        preco = float(input('Preço do item: '))

        print(f'O item de preço R${preco:.2f} somado à {imposto}% de imposto é {soma_imposto(taxa_imposto= imposto, custo= preco):.2f}')
else:
    print('Não entendi, tchau...')