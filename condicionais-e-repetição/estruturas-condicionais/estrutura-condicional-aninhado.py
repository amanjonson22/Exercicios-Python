conta = input('Qual sua conta?\n- Conta Normal(normal)\n- Conta Universitária(uni)\n\n').lower()
conta_normal = False
conta_universitária = False


if conta == 'normal':
    conta_normal = True
elif conta == 'uni':
    conta_universitária = True

saldo = 2000
cheque_especial = 450

if conta_normal:
    saque = int(input('Quanto você quer sacar?\n'))
    if saldo >= saque:
        print('Saque realizado com sucesso')
        print(f'Seu novo saldo é: {saldo - saque}')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com cheque especial')
        print(f'Seu novo saldo é: {(saldo + cheque_especial) - saque}')
    else:
        print('Saldo insuficiente')
elif conta_universitária:
    saque = int(input('Quanto você quer sacar?\n'))
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    else:
        print('Saldo insuficiente')
else:
    print('Sistema não reconheceu seu tipo de conta, entre em contato com o gerente')