#Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def conversao_pm(hora24):
    hora12 = hora24 - 12
    return hora12

def saida_conversao(hora24, minuto):
    if minuto <= 9:
        minuto = '0' + str(minuto)

    if hora24 < 12:
        hora12 = hora24
        hora12 = '0' + str(hora12)
        print(f'A hora é {hora12}:{minuto} A.M.')
        return
    
    elif hora24 == 12:
        hora12 = hora24
        print(f'A hora é {hora12}:{minuto} P.M.')
        return
    
    elif hora24 == 24:
        hora12 = 0
        print(f'A hora é {hora12}:{minuto} A.M.')
        return
    
    elif hora24 > 12 or hora24 < 24:
        hora12 = conversao_pm(hora24)
        
        if hora12 <= 10:
            hora12 = '0' + str(hora12)
        
        print(f'A hora é {hora12}:{minuto} P.M.')
        return
    
    else:
        print('Erro')
        return

while True:
    menu = input('''
BEM-VINDO À CONVERSÃO DE HORA PARA A.M. E P.M.
                 
[c] Converter
[s] Sair
                 
=> ''')
    if menu == 'c':
        hora24 = int(input('Quantas horas? '))
        if hora24 > 24 or hora24 <= 0:
            print('Erro, a hora é maior que 24.')
        else:
            minuto = int(input('Quantos minutos? '))
        
            if minuto >= 60 or minuto <= 0:
                print('Erro, o minuto é maior que 60.')
        
            else:
                print()
                saida_conversao(hora24, minuto)
                print('='*30)
    
    elif menu == 's':
        print('Até logo!')
        break
    
    else:
        print('Erro')