#usa set para eliminar itens duplicados
print('\nAprendendo o comando set()\n')
numeros = set([1,2,3,1,3,4])
print(numeros)

letras = set('abacaxi')
print(letras)

carros = set(('palio', 'gol','celta','palio'))
print(carros)

linguagens = {'python', 'java', 'python'}
print(linguagens)

#acessando itens
print('\nAcessando itens\n')
numeros = {1,2,3,4,1,2}

numeros = list(numeros)

print(numeros[0])

#metodos do set
print('\nMétodos do set\n')
#.union
print('\n.union\n')
conjunto_a = {1,2}
conjunto_b = {3,4}

print(conjunto_a.union(conjunto_b))

#.intersection
print('\n.intersection\n')
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.intersection(conjunto_b))

#.difference
print('\n.difference\n')
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

#.symmetric_difference
print('\n.symmetric_difference\n')
print(conjunto_a.symmetric_difference(conjunto_b))

#.issubset
print('\n.issubset\n')
conjunto_a = {1,2,3}
conjunto_b = {6,5,2,3,1,4,8}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

#.issuperset
print('\n.issuperset\n')
print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

#.isdisjoint
print('\n.isdisjoint\n')
conjunto_a = {1,2,3,4}
conjunto_b = {5,6,7,8}
conjunto_c = {1,0}

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))

#.add
print('\n.add\n')
sorteio = {1,23}

sorteio.add(25)
print(sorteio)

sorteio.add(42)
print(sorteio)

sorteio.add(25)
print(sorteio)

#.discard
print('\n.discard\n')
numeros = {1,2,2,3,4,5,2,6,7,5,5,8,9,10,16,11,12,13,14,15,16,17,18,19,20}

print(numeros)

numeros.discard(1)
print(numeros)

numeros.discard(45)
print(numeros)

#.pop
print('\n.pop\n')

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

print(numeros)
print(numeros.pop())
print(numeros.pop())

print(numeros)

#.remove
print('\n.remove\n')

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}
print(numeros)

print(numeros.remove(5))
#Usar em um item que não existe, dá erro
print(numeros)

#.len
print('\n.len\n')

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}
print(len(numeros))

#.in
print('\n.in\n')
numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

print(1 in numeros)
print(10 in numeros)