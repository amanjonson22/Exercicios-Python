import random

def menu():
    escolha = input('''
=============================================
Bem-Vindo ao Jogo da Adivinhação!

Você terá chutes para adivinhar um número.

[j] Jogar
[s] Sair
          
=> ''')
    return escolha

def jogo(numero):
    tentativas = []

    while True:
        numero = str(numero)

        chute = input('Digite um número de 0-9: ')

        posicao = 1

        for digito in numero:
            if chute == digito:
                print(f'O dígito {chute} na posição {posicao}')
                tentativas.append({'chute': chute, 'posicao': posicao})
            posicao += 1
        
        print(f'Seus números são: {tentativas}')

        if len(tentativas) == len(numero):
            chute_numero = input('Qual o número? ')
            if chute_numero == numero:
                print('Parabéns, você acertou!')
                break
            else:
                print('Você errou, continue tentando')
            
def main():
    while True:
        opcao = menu()
        
        if opcao == 'j':
            numero = random.randint(1, 1000)
            jogo(numero)
        
        elif opcao == 's':
            break

        else: 
            print('Não entendi')

main()