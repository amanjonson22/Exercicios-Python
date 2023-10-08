class Pai:
    def __init__(self, cor_olhos, cor_pele, bens, dividas, nome):
        self.cor_olhos = cor_olhos
        self.cor_pele = cor_pele
        self.bens = bens
        self.dividas = dividas
        self.nome = nome

    def andar(self):
        print(f"O {self.nome} está andando")
    
    def gostoEsportes(self, esportes):
        print(f"O {self.nome} gosta de {esportes}")
    
    def propriedades(self):
        print(f"O {self.nome} tem essas propriedades: {self.bens}. Mas também tem essas dívidas: {self.dividas}")

    def caracteristicas(self):
        print(f"As características do {self.nome} são: cor do olho: {self.cor_olhos} e cor de pele: {self.cor_pele}")
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Filho(Pai):
    def __init__(self, cor_olhos, cor_pele, bens, dividas, estudos, nome):
        super().__init__(cor_olhos, cor_pele, bens, dividas, nome)
        self.estudos = estudos

    def estudar(self):
        print(f"O {self.nome}  estuda: {self.estudos}")
    
class Neto(Filho):
    pass

pai = Pai(cor_olhos="azul", cor_pele="parda", bens="Casa, carro", dividas= "Nenhuma", nome="Abreu")
filho = Filho(cor_olhos="azul", cor_pele="parda", bens="Casa, carro", dividas="Faculdade", estudos="Agronomia", nome= "Marcelo")
neto = Neto(cor_olhos="marrom", cor_pele="parda", bens="Casa, carro", dividas="Faculdade", estudos="Teatro", nome= "Fernando")

print(pai)
print(filho)
print(neto)

pai.andar()
filho.caracteristicas()
neto.gostoEsportes("Vôlei, Futebol")
filho.propriedades()
