#tupla é irmã da lista
#tuplas são imutáveis
#sempre usar a vírgula no final


frutas = ("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1, 2 , 3, 4])

pais = ("Brasil",)

print(type(pais), type(numeros), type(letras), type(frutas))

print(frutas[1])

print(frutas[-2])

matriz = (
    (1, 'a', 2),
    ('b', 3, 4),
    (5, 6, 'c'),
)

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

#usa tupla para valor imutável

tupla = (1, 2, 3, 4, 5, 6, 7,)

print(tupla[2:])
print(tupla[:2])
print(tupla[1:3])
print(tupla[0:3:2])
print(tupla[::])
print(tupla[::-1])

#iteração
numero = (1,2,3,4,5,6,7,8,)

for indice, n in enumerate(numero):
    print(f'{indice}: {numero}')

#tupla tem: .count; .index; . len;