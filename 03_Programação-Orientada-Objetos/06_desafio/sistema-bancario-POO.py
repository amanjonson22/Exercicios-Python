def menu(): 
    menu = '''
====================== MENU ======================
Bem-vindo! Que operação deseja realizar?

[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo usuário
[5] Nova Conta
[6] Listar Contas
[7] Sair

=> '''
    return input(menu)

def saque(*, limite_saques, numero_saques, saldo, extrato_str, limite, valor_saque):
    if numero_saques < limite_saques:
        if valor_saque <= limite and valor_saque <= saldo and valor_saque > 0: 
            numero_saques += 1
            saldo -= valor_saque
            extrato_str = extrato_str + 'Saque: R$ ' + str(valor_saque) + '\n'
            print(f'Saque de R$ {valor_saque:.2f} efetuado com sucesso')
            
        else:
            if valor_saque > saldo:
                print('Operação inválida! Você não tem saldo suficiente.')
            elif valor_saque > limite:
                print('Operação inválida! O valor do saque excede o limite.')

            else:
                print('Operação falhou! O valor informado é inválido.')
    else:
        print('Seu limite de saques já foi atingido.')

    return saldo, extrato_str

def depositar(saldo, valor_depósito, extrato_str, /):   
    if valor_depósito <= 0:   
        print('O valor informado é inválido.') 
        
    else:
        saldo += valor_depósito
        extrato_str = extrato_str + 'Depósito: R$ ' + str(valor_depósito) + '\n'
        print(f'Depósito de R$ {valor_depósito:.2f} efetuado com sucesso')
    
    return saldo, extrato_str

def extrato(saldo,/,*, extrato_str):    
    print('\n==================== Extrato ====================\n')        
    print('Não foram realizadas movimentações.' if not extrato_str else extrato_str)
    print(f'\nSeu saldo atual é: R$ {saldo}')
    print('\n =================================================')

def criar_usuario(usuarios):
    cpf = input('CPF(somente número): ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('\nJá existe um usuário com esse CPF')
        return
    
    nome = input('Nome completo: ')
    data_nascimento = input('Data de nascimento (dd/mm/aaaa): ')
    endereco = input('Endereço (logradouro, nro - bairro - cidade/sigla do estado): ')

    usuarios.append({'nome': nome, 'data_nasimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print('\nUsuário cadastrado com sucesso')

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta_corrente(agencia, numero_conta, usuarios):
    cpf = input('CPF do usuário: ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('\nConta criada com sucesso')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('\nUsuário não encontrado.')

def listar_contas(contas):
    for conta in contas:
        linha = f'''

            Agência: \t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print('#'*30)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato_str = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == '1':
            print('\nDepósito\n')
            valor_depósito = float(input('Valor do depósito: '))
        
            saldo, extrato_str = depositar(saldo, valor_depósito, extrato_str)

        elif opcao == '2':
            print('\nSaque\n')
            
            valor_saque = float(input('Valor do saque: '))
            saldo, extrato_str = saque(
                saldo= saldo,
                valor_saque= valor_saque,
                extrato_str= extrato_str,
                limite= limite,
                limite_saques= LIMITE_SAQUES,
                numero_saques= numero_saques
            )   

        elif opcao == '3':
            extrato(saldo, extrato_str= extrato_str)
        
        elif opcao == '4':
            criar_usuario(usuarios)
        
        elif opcao == '5':
            numero_contas = len(contas) + 1
            conta = criar_conta_corrente(AGENCIA, numero_contas, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == '6':
            listar_contas(contas)

        elif opcao == '7':
            break

        else:
            print('\nOperação inválida, por favor selecione novamente a operação desejada.\n')

main()
