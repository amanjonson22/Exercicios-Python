dividendo = int(input('Número: '))
numero_digitado = dividendo
quociente = 1
lista = []

while quociente >= 1:
    resto = dividendo%2
    lista.append(resto)
    quociente = dividendo//2
    dividendo = quociente

binario = ''.join(str(i) for i in lista )
print('O número', numero_digitado, 'em binário é: ', binario)