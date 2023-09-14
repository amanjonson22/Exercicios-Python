#Faça um programa para imprimir:
#    1
#    2   2
#    3   3   3
#    .....
#    n   n   n   n   n   n  ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def repeticao(n):
    x = 1
    while x <= n:
        for n1 in range(n):
            for n2 in range(x):
                print(x, end=' ')
            x += 1
            print()
        
n = int(input('Número: '))
repeticao(n)