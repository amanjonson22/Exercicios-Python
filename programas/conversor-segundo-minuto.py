menu = '''
################## Menu ##################
Olá, bem-vindo ao conversor segundo-minuto!
Escolha sua conversão:

[1] - Segundo para minuto
[2] - Minuto para segundos
[3] - Soma de tempo
[4] - Sair

=> '''

while True:
    escolha = input(menu)
    
    if escolha == '1':
        print('\nSegundo para minuto\n')
        segundo_converter = int(input('Quantos segundos? '))
        minuto = 0
        segundo_convertido = segundo_converter

        while segundo_convertido >= 60:
            segundo_convertido -= 60
            minuto += 1
        
        print(f'{segundo_converter} s em minutos é: {minuto} min e {segundo_convertido} s')
    
    elif escolha == '2':
        print('\nMinuto para segundo\n')
        minuto_converter = int(input('Quantos minutos? '))
        segundo = minuto_converter * 60

        print(f'{minuto_converter} min em segundos é: {segundo} s')
    
    elif escolha == '3':
        print('\nSoma de tempo\n')
        minuto_1 = int(input('Minuto: '))
        segundo_1 = int(input('Segundo: '))

        minuto_2 = int(input('Minuto: '))
        segundo_2 = int(input('Segundo: '))

        resultado_segundos = segundo_1 + segundo_2
        resultado_minutos = minuto_1 + minuto_2
        
        while resultado_segundos >= 60:
            resultado_minutos += 1
            resultado_segundos -= 60
        
        print(f'{minuto_1}min {segundo_1}s + {minuto_2}min {segundo_2}s = {resultado_minutos}min {resultado_segundos}s')

    elif escolha == '4':
        print('Tchau!')
        break
    
    else:
        print('\nNão reconheço esse comando. Tente novamente.')

        

        