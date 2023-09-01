def again():
    calculo_novamente = input('\nVocê gostaria de calcular novamente? \nS para sim\nN para não\n\n').upper()
    if calculo_novamente == 'S':
        calculo()
    elif calculo_novamente == 'N':
        print('Tchau tchau!')
        pass
    else:
        print('Não entendi')
        again()


def calculo():
    operador = 0
    while operador != 'sair':
        numero_1 = float(input('\nDigite um número: '))
        numero_2 = float(input('Digite o segundo número: '))
        
        operador = input('Selecione um operador:\n\n + para somar\n - para subtração\n * para multiplicação\n / para divisão\n ** para potências\n\n Sair para sair\n\n').lower()
    
        if operador == '+':
            print(f'\n{numero_1} + {numero_2} = {numero_1 + numero_2}')
            again ()
        elif operador == '-':
            print(f'\n{numero_1} - {numero_2} = {numero_1 - numero_2}')
            again ()
        elif operador == '*':
            print(f'\n{numero_1} * {numero_2} = {numero_1 * numero_2}')
            again ()
        elif operador == '/':
            print(f'\n{numero_1} / {numero_2} = {numero_1 / numero_2}')
            again ()
        elif operador == '**':
            print(f'\n{numero_1} ** {numero_2} = {numero_1 ** numero_2}')
            again ()
        elif operador == 'sair':
            print('\nEntendi, tchau tchau!')
            pass
        else:
            print('\nNão entendi\n')
            calculo()
    pass

def main():
    print('Bem-vindo à calculadora mega básica! Você só pode calcular dois números e poucas operações!\n')
    calculo()
    pass

main()