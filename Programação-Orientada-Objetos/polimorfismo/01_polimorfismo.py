class Passaro:
    def voar(self): 
        print("Voando...")

class Pardal(Passaro): 
    def voar(self):
        super().voar()
        #print("Pardal voa")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

# FIXME: exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando")

#O conceito de polimorfismo está aqui
def plano_de_voo(obj):
    obj.voar()


plano_de_voo(Pardal())
plano_de_voo(Avestruz())
plano_de_voo(Aviao())