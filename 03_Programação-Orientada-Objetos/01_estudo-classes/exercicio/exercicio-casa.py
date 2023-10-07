class Casa:
    def __init__(self, cor_parede, numero_quartos, quantidade_vagas, numero_banheiros, altura_teto, endereco: str, proprietario, jardim: bool, alugada: False, inquilino= None, valor_aluguel= 0):
        self.cor_parede = cor_parede
        self.numero_quartos = numero_quartos
        self.quantidade_vagas = quantidade_vagas
        self.numero_banheiros = numero_banheiros
        self.altura_teto = altura_teto
        self.endereco = endereco
        self.proprietario = proprietario

        if alugada == False:
            self.alugada = "Não é alugada"
            self.inquilino = "Ninguém aluga aqui!"
            self.valor_aluguel = "Não há valor, pois ninguém aluga aqui!"
        
        else:
            self.alugada = "É alugada"
            self.valor_aluguel = valor_aluguel
            self.inquilino = inquilino

        if jardim == True:
            self.jardim = "Tem jardim!"
        
        else:
            self.jardim = "Não tem jardim!"
        
    
    def pintar_parede(self, cor_parede):
        self.cor_parede = cor_parede
        print("Parede pintada! Sua nova cor é " + self.cor_parede)
    
    def construir_quartos(self):
        print(f"Sua casa tem {self.numero_quartos} quartos")

    def construir_banheiros(self):
        print(f"Sua casa tem {self.numero_banheiros} banheiros")
    
    def construir_garagem(self):
        print(f"Sua casa tem {self.quantidade_vagas} vagas")

    def construir_teto(self):
        if self.altura_teto <= 3 and self.altura_teto > 1.7:
            print("Sua casa tem o pé direito aceitável")
        elif self.altura_teto > 3:
            print("Sua casa tem o pé direito alto!")
        else:
            print("Isso não é habitável...")
    
    def tem_jardim(self):
        if self.jardim == "Tem jardim!":
            print("Sua casa tem jardim, pense em fazer umas hortinhas!")
        else:
            print("Que tristeza, sua casa não tem jardim...")
    
    def localizacao_casa(self):
        print(f"Parabéns pela sua nova casa! O endereço dela é {self.endereco}")
    
    def alugar_casa(self, inquilino, valor_aluguel):
        self.alugada = True
        self.inquilino = inquilino
        self.valor_aluguel = valor_aluguel
        print(f"Parabéns, você está alugando sua casa. O seu novo inquilino é {self.inquilino} e ele te paga R${self.valor_aluguel} todo mês.")
    
    def vender_casa(self, proprietario):
        print(f"Parabéns, você vendeu sua casa. A propriedade mudou da posse de {self.proprietario} para {proprietario}. Não se esqueça de entregar as chaves, ein!")
        self.proprietario = proprietario
    
    def __str__(self):
        return f"{self.__class__.__name__}: \nCor da parede: {self.cor_parede}\nQuantidade de quartos {self.numero_quartos}\nQuantidade de vagas: {self.quantidade_vagas}\nQuantidade de banheiros: {self.numero_banheiros}\nAltura do pé direito: {self.altura_teto}\nTem jardim: {self.jardim}\nProprietário: {self.proprietario}\nEndereço: {self.endereco}\nAlugada? {self.alugada}\nInquilino: {self.inquilino}\nValor do aluguel: {self.valor_aluguel}"

def menu():
    escolha = input("""       
[1] Vender
[2] Pintar parede
[3] Alugar
[4] Relembrar informações
[5] Sair
          
=>""")
    return escolha

print("""Bem-Vindo ao programa de Casas
    
Estamos construindo e definindo características de casas, além de comprar e vender.
""")

parede = input("\nQual a cor da parede? ")
quartos = int(input("\nQuantos quartos? "))
vagas = int(input("\nQuantas vagas na garagem? "))
banheiro = int(input("\nQuantos banheiros? "))
pe_direito = float(input("\nQual altura do pé direito você quer? "))
localizacao = input("\nQual o endereço da casa? ")
dono = input("\nQuem é o dono da casa? ")
while True:
    tem_jardim = input("\nTem jardim? \n[s] Sim\n[n] Não\n=> ").lower()
    if tem_jardim == 's':
        grama = True
        break

    elif tem_jardim == 'n':
        grama = False
        break
            
    else: print("Isso não é uma opção...")


casa = Casa(cor_parede= parede, numero_quartos= quartos, quantidade_vagas= vagas, numero_banheiros= banheiro, altura_teto= pe_direito, endereco= localizacao, proprietario= dono, jardim= grama, alugada= False, inquilino= None, valor_aluguel= 0)

print()
casa.pintar_parede(parede)
casa.construir_banheiros()
casa.construir_quartos()
casa.construir_garagem()
casa.construir_teto()
casa.tem_jardim()
print()
casa.localizacao_casa()

while True:
    escolha = menu()

    if escolha == '1':
        novo_dono = input("Quem é o novo dono? ")
        
        casa.vender_casa(proprietario= novo_dono)

    elif escolha == '2':
        nova_tinta = input("Qual a nova cor que você quer pintar a parede? ")

        casa.pintar_parede(cor_parede= nova_tinta)

    elif escolha == '3':
        novo_inquilino = input("Para quem você está alugando? ")
        preco = int(input("Qual o valor do aluguel? R$"))

        casa.alugar_casa(inquilino=novo_inquilino, valor_aluguel=preco)

    elif escolha == '4':
        print(casa)

    elif escolha == '5':
        print("Até logo!")
        break

    else:
        print("\nNão entendi, pode repetir?\n")