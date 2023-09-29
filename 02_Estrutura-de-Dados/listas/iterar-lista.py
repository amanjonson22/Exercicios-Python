carros = ['gol', 'celta', 'voyage']

for carro in carros:
    print(carro)

#enumerate

for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')

#compreensão de listas: criar uma lista nova com base em uma existente
###jeito normal
numeros = [1, 30, 21, 2, 9, 65, 34, 28, 32]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares, numeros)

#####comprehension
numeros = [1, 32, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)
