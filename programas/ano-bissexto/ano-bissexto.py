while True:
    escolha = input("Você quer continuar checando?\n[s] Sim\n[n] Não").lower()
    if escolha == 's':
        ano = int(input('Qual o ano? '))
        resultado = True

        resultado = (ano % 4 == 0) and (ano % 100 > 0) or (ano % 400 == 0)
        print(f'O ano {ano} é bissexto? {"sim" if resultado == True else "não"}')
    
    else:
        print("Entendido! Até a próxima!")
        break