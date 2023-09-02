while True:
    opcao = int(input('Informe um número: '))

# break quebra o while e o for e encerra o looping.    
    if opcao == 10:
        break

# continue pula aquela opção. Nesse caso abaixo, não imprimirá os números pares.
    if opcao % 2 == 0:
        continue

    

    print(opcao)

lista_pares = []

for numero in range(21):
    if numero % 2 == 0:
        continue
    print(numero, end=' ')