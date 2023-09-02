import random

def numero_usuario():
    numero_usuario = random.randint(100000, 999999)
    return str(numero_usuario)

def senha():
    senha_conta = input('Qual a senha?\n ')
    return senha_conta

def username():
    username = input('Qual seu nome de usuário?\n ')
    usuario = []
    numero_de_usuario = numero_usuario()
    senha_de_usuario = senha()
    usuario.append(username)
    usuario.append(numero_de_usuario)
    usuario.append(senha_de_usuario)
    print(f'Seu nome de usuário é {username}, seu número é {numero_de_usuario} e sua senha {senha_de_usuario}.')
    return usuario

def conta(username):
    print(f'Bem-vindo {username[0]}')
    pass


def login(username):
    usuario_digitado = input('Usuário(username ou número de usuário): ')
    senha_digitada = input('Senha: ')
    informações_usuário = username
    if usuario_digitado == informações_usuário[0] or usuario_digitado == informações_usuário[1] and senha_digitada == informações_usuário[2]:
        conta(informações_usuário)
    else:
        print('Você não digitou as informações corretas...')
    return informações_usuário

def criar_conta():
    conta = username()
    return conta

def main():
    print('Olá, seja bem-vindo! O que você deseja?\n')
    decisao = 0
    while decisao != 'sair':
        decisao = input('- Criar conta(criar)\n\n - Login(login)\n\n - Sair(sair)\n').lower()
        if decisao == 'criar':
            conta = criar_conta()
        elif decisao == 'login':
            login(conta)
        elif decisao == 'sair':
            print('Tchau!')
    pass

main()




