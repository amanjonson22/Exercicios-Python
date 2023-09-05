menu = '''
Bem-vindo! Que operação deseja realizar?

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair


=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == '1':
        
        print('\nDepósito\n')
        
        valor_depósito = float(input('Valor: '))
        
        if valor_depósito <= 0:
            
            print('O valor informado é inválido.')
        
        else:
            
            saldo += valor_depósito
            
            extrato = extrato + 'Depósito: R$ ' + str(valor_depósito) + '\n'
            
            print(f'Depósito de R$ {valor_depósito:.2f} efetuado com sucesso')
    
    elif opcao == '2':
        
        print('\nSaque\n')
        
        if numero_saques < LIMITE_SAQUES:
            
            valor_saque = float(input('Valor do saque: '))
            
            if valor_saque <= limite and valor_saque <= saldo and valor_saque > 0:
                
                numero_saques += 1
                
                saldo -= valor_saque
                
                extrato = extrato + 'Saque: R$ ' + str(valor_saque) + '\n'
                
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

    elif opcao == '3':
        
        print('\n==================== Extrato ====================\n')
        
        print('Não foram realizadas movimentações.' if not extrato else extrato)

        print(f'\nSeu saldo atual é: R$ {saldo}')

        print('\n =================================================')

    elif opcao == '4':
        
        break

    else:
        print('\nOperação inválida, por favor selecione novamente a operação desejada.\n')
