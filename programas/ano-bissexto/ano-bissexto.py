while True:
    escolha = input("Você quer continuar checando?\n[s] Sim\n[n] Não\n=>").lower()
    if escolha == 's':
        ano = int(input('\nQual o ano? '))
        resultado = True

        resultado = (ano % 4 == 0) and (ano % 100 > 0) or (ano % 400 == 0)
        print(f'\nO ano {ano} é bissexto? {"sim" if resultado == True else "não"}')
    
    elif escolha == 'n':
        print("\nEntendido! Até a próxima!")
        break

    else: print('\nNão entendi...')