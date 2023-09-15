class Cachorro:
    def __init__(self, nome, cor, adestrado = True): #sempre executado na instanciação
        print('Inicializando classe...')
        self.nome = nome #atributo
        self.cor = cor #atributo
        self.adestrado = adestrado #atributo
    
    def latir(self):
        print('auau')

    def __del__(self): #executado no final
        print('Destruindo instância...')


c = Cachorro('Junior', 'amarelo', adestrado=False)
c.latir()

print()
print()
print()

del c

print('oi')
print('oi')