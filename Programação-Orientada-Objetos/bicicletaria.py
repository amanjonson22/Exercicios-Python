#João informe: cor, modelo, ano e valor da bicicleta vendida. A bicicleta pode buzinar, parar e correr.
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor): #self é a instancia do objeto
        self.cor = cor #atributo
        self.modelo = modelo #atributo
        self.ano = ano #atributo
        self.valor = valor #atributo

    def buzinar(self): #método
        print('Bi biii')
    
    def parar(self): #método
        print('Parada')
    
    def correr(self): #método
        print('Correndo!')
    
cor_vendida = input('Cor: ')
modelo_vendido = input('Modelo: ')
ano_vendido = input('Ano: ')
valor_vendido = float(input('Valor: R$'))

bicleta_vendida = Bicicleta(cor_vendida, modelo_vendido, ano_vendido, valor_vendido)

bicleta_vendida.buzinar()
bicleta_vendida.correr()
bicleta_vendida.parar()

print(f'A cor da bicicleta é: {bicleta_vendida.cor}')
print(f'O modelo da bicicleta é: {bicleta_vendida.modelo}')
print(f'O ano da venda é: {bicleta_vendida.ano}')
print(f'O valor que foi vendido é: R${bicleta_vendida.valor:.2f}')