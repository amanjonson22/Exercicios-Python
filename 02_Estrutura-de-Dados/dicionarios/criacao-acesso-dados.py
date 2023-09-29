#declarando dicionários
print('\ndeclarando dicionários\n')
pessoa = {'nome': 'Amanda', 'idade': 20}
print(pessoa)

pessoa_2 = dict(nome = 'Amanda', idade = 20)

pessoa['telefone'] = '3947-4364'

print(pessoa)
print(pessoa_2)

#acessando o valor
print('\nacessando valores\n')
dados = {'nome': 'Amanda', 'idade': 20, 'telefone': '3245-2323'}

print(dados['nome'])
print(dados['idade'])
print(dados['telefone'])

print(dados)

#substituindo valores
print(dados['nome'])
print(dados['idade'])
print(dados['telefone'])

print(dados)

dados['nome'] = 'Roberta'
dados['idade'] = 22
dados['telefone'] = '9943-2351'

print(dados['nome'])
print(dados['idade'])
print(dados['telefone'])
print(dados)

#dicionários aninhados
print('\ndicionários aninhado\n')
contatos = {
    'alice@gmail.com': {'nome': 'Alice', 'telefone': '3214-4321'},
    'gertrude@gmail.com': {'nome': 'Gertrude', 'telefone': '2314-6534'},
    'melanie@gmail.com': {'nome': 'Melanie', 'telefone': '6543-2314'},
    'roberta@gmail.com': {'nome': 'Roberta', 'telefone': '3421-6523'},
}

print(contatos)
print(contatos['gertrude@gmail.com']['telefone'])
print(contatos['melanie@gmail.com']['nome'])
print(contatos['roberta@gmail.com'])

print('\nGrande dicionário aninhado\n')

grande_dicionario_aninhado = {
    'alice_batista@gmail.com': {'nome': 'Alice', 'sobrenome':'Batista', 'extra': {'contato':{'familia': {'mãe': '99834-2314', 'pai': '99217-2145'},'individuo':{'telefone':'98435-1235'}},'moradia':{'rua':'Rua Luís Inácio','numero':'1313','cidade':'São José de Botiviriva'}}}
}

print(grande_dicionario_aninhado['alice_batista@gmail.com']['extra']['contato']['familia']['mãe'])

#Iterar dicionários
print('\nIterar dicionários\n')
for chave in contatos:
    print(chave, contatos[chave])

print()

for chave, valor in contatos.items():
    print(chave, valor)

