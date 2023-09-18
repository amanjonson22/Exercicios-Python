def conversao(dividendo):
    quociente = 1
    lista = []

    while quociente >= 1:
        resto = dividendo%2
        lista.append(resto)
        quociente = dividendo//2
        dividendo = quociente

    lista = lista[::-1]
    binario = ''.join(str(i) for i in lista )
    print('O número', dividendo, 'em binário é: ', binario)



def menu():
    menu = input('''================ Bem-Vindo ================

[c] Conversão
[s] Sair

=> ''')
    return menu

def main():
    while True:
        opcao = menu()
        if opcao == 'c':
            dividendo = int(input('Número: '))
            conversao(dividendo)
        
        elif opcao == 's':
            break

        else:
            print('Erro. Tente novamente.')

main()