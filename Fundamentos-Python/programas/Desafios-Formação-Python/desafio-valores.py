N = int(input())

while(N > 0):
    numero_A = input()
    numero_B = input()

    if numero_A.endswith(numero_B):
        print('encaixa')
    else: 
        print('nao encaixa')
    
    N -= 1