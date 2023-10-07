class Casa:
    def __init__(self, cor_parede, numero_quartos, quantidade_vagas, numero_banheiros, altura_teto, numero_casa, jardim: bool):
        self.cor_parede = cor_parede
        self.numero_quartos = numero_quartos
        self.quantidade_vagas = quantidade_vagas
        self.numero_banheiros = numero_banheiros
        self.altura_teto = altura_teto
        self.jardim = jardim
        self.numero_casa = numero_casa
    
    def pintar_parede(self):
        print("Parede pintada! Sua nova cor é " + self.cor_parede)
    
    def construir_quartos(self):
        print(f"Sua casa tem {self.numero_quartos}")

    def construir_banheiros(self):
        print(f"Sua casa tem {self.numero_banheiros}")
    
    def construir_garagem(self):
        print(f"Sua casa tem {self.quantidade_vagas}")

    def construir_teto(self):
        if self.altura_teto <= 3 and self.altura_teto > 1.7:
            print("Sua casa tem o pé direito aceitável")
        elif self.altura_teto > 3:
            print("Sua casa tem o pé direito alto!")
        else:
            print("Isso não é habitável...")
    
    def tem_jardim(self):
        if self.jardim == True:
            print("Sua casa tem jardim, pense em fazer umas hortinhas!")
        else:
            print("Que tristeza, sua casa não tem jardim...")
    
    def endereco(self):
        print(f"Parabéns pela sua nova casa! O número dela na rua é {self.numero_casa}")


casa1 = Casa(cor_parede= "Vinho", numero_quartos= 4, quantidade_vagas= 2, numero_banheiros= 3, altura_teto= 4, numero_casa= 120, jardim= True)

casa2 = Casa(cor_parede= "Branca", numero_quartos= 2, quantidade_vagas= 0, numero_banheiros= 1, altura_teto= 2.25, numero_casa= 112, jardim= False)

casa3 = Casa(cor_parede= "Branca", numero_quartos= 2, quantidade_vagas= 0, numero_banheiros= 1, altura_teto= 1.5, numero_casa= 113, jardim= False)

casa1.endereco()
casa2.endereco()

casa1.construir_teto()
casa2.construir_teto()
casa3.construir_teto()

casa1.pintar_parede()

print(casa1.numero_banheiros)
print(casa2.numero_quartos)
print(casa3.quantidade_vagas)