#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def positivo_negativo(n):
    if n > 0:
        print('P')
    elif n < 0:
        print('N')
    else: 
        print('Zero')
    
    return

quantidade_testes = int(input('Quantidade de testes: '))

for numero in range(quantidade_testes):
    n = int(input('Número: '))
    positivo_negativo(n)