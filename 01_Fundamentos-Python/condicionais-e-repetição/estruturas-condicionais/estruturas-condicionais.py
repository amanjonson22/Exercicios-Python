MAIOR_IDADE = 21
IDADE_ESPECIAL = 18

idade = int(input('Informe sua idade: '))

if idade >= IDADE_ESPECIAL:
    print('Maior de idade, pode tirar a CNH.')

if idade < IDADE_ESPECIAL:
    print('Ainda não pode tirar a CNH')

if idade >= IDADE_ESPECIAL:
    print('Maior de idade, pode tirar a CNH.')
else: 
    print('Ainda não pode tirar a CNH')

if idade >= MAIOR_IDADE:
    print('Pode tirar a CNH e beber em todos os países do mundo! Você é mundialmente maior de idade')
elif idade >= IDADE_ESPECIAL:
    print('Maior de idade no Brasil, mas não pode beber em alguns países afora')
else:
    print('Você é menor de idade, não pode tirar CNH nem beber.')