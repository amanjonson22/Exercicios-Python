from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando TV")
        print("Ligado")

    def desligar(self):
        print("Desligando TV")
        print("Desligado")

    @property
    def marca(self):
        return "Philco"



class ControleAC(ControleRemoto):
    def ligar(self):
        print("Ligando Ar Condicionado")
        print("Ligado")
    
    def desligar(self):
        print("Desligando Ar Condicionado")
        print("Desligado")
    
    @property
    def marca(self):
        return "LG"

controle_TV = ControleTV()
controle_TV.ligar()
controle_TV.desligar()
print(controle_TV.marca)

controle_AC = ControleAC()
controle_AC.ligar()
controle_AC.desligar()
print(controle_AC.marca)
