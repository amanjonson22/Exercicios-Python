#Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

def valorPagamento(prestacao, dias_atraso):
    #calcula o valor a ser pago
    if dias_atraso > 0:
        multa = prestacao * 0.03
        atraso = dias_atraso*0.1/100
        valor_atraso = prestacao*atraso
        prestacao = prestacao + multa + valor_atraso
        print(f'Você pagou {prestacao:.2f}')
    
    elif dias_atraso == 0:
        print(f'Você pagou {prestacao:.2f}')

    return float(f'{prestacao:.2f}')

def relatório_dia(relatorio):
    #informa a quantidade de prestações e o valor total da prestação
    print('\nOs pagamentos do dia foram:\n')
    for pagamento in relatorio:
        print(f'R${pagamento}')
    print(f'A quantidade de pagamentos foram {len(relatorio)}')
    return

def main():
    relatorio = []
    while True:
        prestacao = float(input('Informe o valor da prestação: '))
        dias_atraso = int(input('Informe os dias de atraso: '))
        relatorio.append(valorPagamento(prestacao, dias_atraso))

        if prestacao == 0:
            break
    
    relatório_dia(relatorio)

main()