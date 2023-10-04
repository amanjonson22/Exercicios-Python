#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
def reverso_numero():
    numero = input('Digite um número: ')
    print(numero[::-1])

reverso_numero()