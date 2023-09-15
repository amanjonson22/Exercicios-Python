#Se tiver até 500 caracteres, imprime TWEET. Se não, imprime MUTE
T = input()

if len(T) <= 500 and len(T) >= 1:
    print('TWEET')
else:
    print('MUTE')
