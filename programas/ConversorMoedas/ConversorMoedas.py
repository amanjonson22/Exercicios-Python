def dolar():
    valor = float(input("\nQual o valor a converter? \n=> R$"))
    dolar = valor*0.19
    print(f'\nO valor R${valor:.2f} convertido em dólar, usado a cotação de R$1 para US$0.19, resulta em US${dolar:.2f}')

def euro():
    valor = float(input('\nQual o valor a converter? \n=> R$'))
    euro = valor*0.18
    print(f"\nO valor R${valor:.2f} convertido em euros, usado a cotação de R$1 para EU$0.18, resulta em EU${euro:.2f}")

def pesos_argentinos():
    valor = float(input('\nQual o valor a converter? \n=> R$'))
    pesos = valor*67.99
    print(f'\nO valor R${valor:.2f} convertido em pesos argentinos, usado a cotação de R$1 para ARS$67.99, resulta em ARS${pesos:.2f}')
    

def menu():
    escolha = input("""
Bem-Vindo ao Conversor de Valores
    
Lembre-se, estamos convertendo real para alguma das moedas abaixo:
          
[1] Dólar
[2] Euro
[3] Pesos Argentinos
[4] Sair
          
=>""")
    return escolha

while True:
    escolha = menu()
    if escolha == '1':
        dolar()
    
    elif escolha == '2':
        euro()        

    elif escolha == '3':
        pesos_argentinos()        

    elif escolha == '4':
        print('Tchau')
        break

    else:
        print('\nNão entendi, tente novamente.\n')