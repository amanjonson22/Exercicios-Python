nome = 'Amanda'
idade = 20
profissão = 'Piloto'
linguagem = 'Python'

PI = 3.14159

dados = {'nome': 'Amanda', 'idade': 20}

print('Nome: %s Idade: %d' % (nome, idade))
print('Nome: {} Idade: {}'.format(nome, idade))

print('Nome: {0} Idade: {1}'.format(nome, idade))
print('Nome: {nome} Idade: {idade}'.format(nome = nome, idade = idade))
print('Nome: {nome} Idade: {idade}'.format(**dados))

print(f'Nome: {nome} Idade: {idade}')

print(f'Nome {nome}, Idade: {idade}, Pi: {PI:.2f}')
