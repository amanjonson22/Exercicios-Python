#.append: adiciona itens
lista = []

lista.append('olá')
lista.append(1)
lista.append([1,2,3])

print(lista)

#.clear: para limpar a lista

lista_01 = [1, 12, 'oi', [22,'vezes',2,42]]

print(lista_01)

lista_01.clear()

print(lista_01)

#.copy(): retorna uma lista igual em uma instância diferente, fazendo com que o que faz na lista 1, não reflete na lista 2
lista_02 = ['a','vida','é','bela']

lista_03 = lista_02.copy()

print(lista_02)
print(lista_03)

lista_02.append('!')
lista_03.append('!!!')

print(lista_02)
print(lista_03)

#.count(): Para contar quantas vezes um objeto aparece em uma lista
letras = ['a','r','a','r','a']

print(letras.count('a'))
print(letras.count('r'))

#.extend(): adiciona novos elementos sem necessitar do append. Une duas listas
idiomas = ['italiano', 'francês', 'português','inglês']

print(idiomas)

idiomas.extend(['noruegues','espanhol','holandes'])

print(idiomas)

#.index(): é para saber quando é a primeira vez que aparece o objeto
palavra = ['b','i','s','s','e','x','u','a','l']

print(palavra.index('b'))
print(palavra.index('x'))
print(palavra.index('s'))

#.pop(): retira o ultimo elemento adicionado
idiomas.pop()
print(idiomas)
idiomas.pop()
print(idiomas)
idiomas.pop(0)
print(idiomas)

#.remove(): remove igual o pop, porém, ao invés de passar o indice, passa qual objeto quer ser retirado. retira apenas a primeira ocorrencia que encontrar
idiomas = ['italiano', 'francês', 'português','inglês','noruegues','espanhol','holandes']

idiomas.remove('italiano')
idiomas.remove('espanhol')
print(idiomas)

#.reverse(): espelha a lista
idiomas = ['italiano', 'francês', 'português','inglês','noruegues','espanhol','holandes']
print(idiomas)

idiomas.reverse()
print(idiomas)

#.sort(): organiza a lista
numeros = [1,3,5,2,6,8,1,2,7,3,4,9,0]
numeros.sort()
print(numeros)

#reverse vai ordenar e colocar ao contrário
numeros = [1,3,5,2,6,8,1,2,7,3,4,9,0]
numeros.sort(reverse=True)
print(numeros)

#lambda é uma função anonima que vai ordenar de acordo com o tamanho das palavras.
idiomas = ['italiano', 'francês', 'português','inglês']
idiomas.sort(key=lambda x: len(x))
print(idiomas)

idiomas = ['italiano', 'francês', 'português','inglês']
idiomas.sort(key=lambda x: len(x), reverse=True)
print(idiomas)

#len(): vê o tamanho da lista
#sorted(): função builtin que organiza

lista_04 = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
print(lista_04)