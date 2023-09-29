texto = input('Informe um texto: ')
VOGAIS = 'AEIOU'
quantidade_letras = []

for letra in texto:
    if letra.upper() in VOGAIS:
        quantidade_letras.append(letra)
        print(letra, end='')
else:
    print()
    print('Executa no fim do laço')

print(f'\nA quantidade de vogais é: {len(quantidade_letras)}')
print()