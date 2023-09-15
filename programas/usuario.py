import random

class Usuario:
    def __init__(self, nome, senha, n_usuario):
        self.nome = nome
        self.senha = senha
        self.n_usuario = n_usuario

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

def criar_conta():
    n_usuario = random.randint(100000, 999999)
    nome = input('Nome: ')
    senha = input('Senha: ')
    conta = Usuario(nome, senha, n_usuario)
    print('Sua id é:', conta.n_usuario)
    return conta

def login(conta, nro_user):
    usuario_digitado = input('Usuário(username ou número de usuário): ')
    senha_digitada = input('Senha: ')
    if usuario_digitado == nro_user or usuario_digitado == conta.nome and senha_digitada == conta.senha:
        print('Bem-vindo!')
    else:
        print('Você não digitou as informações corretas...')
    return

def main():
    print('Olá, seja bem-vindo! O que você deseja?\n')
    while True:
        decisao = input('- Criar conta(c)\n\n - Login(l)\n\n - Quem sou eu?(q)\n\n - Sair(s)\n\n=> ').lower()
        if decisao == 'c':
            conta = criar_conta()
            nro_user = conta.n_usuario
        elif decisao == 'l':
            login(conta, nro_user)
        elif decisao == 's':
            print('Tchau!')
            break
        elif decisao == 'q':
            print(conta)
        else:
            print('Não entendi')
    pass

main()