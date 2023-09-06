conta = {
    'nome': '','sobrenome': '', 'email': '', 'senha': ''
}

def criarConta():
    nome = input('Nome: ')
    sobrenome = input('Sobrenome: ')
    email = input('Email: ')
    senha = input('Senha: ')

    conta['nome'] = nome
    conta['sobrenome'] = sobrenome
    conta['email'] = email
    conta['senha'] = senha

    print('\nConta criada com sucesso\n')
    pass

def login():
    email = input('Email: ')
    senha = input('Senha: ')

    if email == conta['email']:
        if senha == conta['senha']:
            print(f'\nBem-Vindo(a) {conta["nome"]}!\n')
        else: 
            print('\nSenha errada\n')
        
    else:
        print('\nEmail errado\n')
    pass
    
    pass

while True:
    escolha = input('''
========== Conta ==========
O que você deseja?
[1] Criar conta
[2] Login
[3] Sair

=> ''')
    
    if escolha == '1':
        criarConta()
    
    elif escolha == '2':
        if conta['email'] == '' and conta['senha'] == '':
            print('\nNão existe conta, tente novamente\n')
        else:
            login()
    elif escolha == '3':
        print('\nAté breve!\n')
        break
    else:
        print('\nNão reconheço esse comando\n')