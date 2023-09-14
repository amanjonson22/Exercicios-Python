#Faça um programa para imprimir:
#    1
#    1   2
#    1   2   3
#    .....
#    1   2   3   ...  n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha

def repeticao(n):
    x = 1
    repetir = 1
    while repetir <= n:
        for n1 in range(n):
            for n2 in range(repetir):
                print(x, end=' ')
                x += 1
            x = 1
            repetir += 1
            print()
        
n = int(input('Número: '))
repeticao(n)