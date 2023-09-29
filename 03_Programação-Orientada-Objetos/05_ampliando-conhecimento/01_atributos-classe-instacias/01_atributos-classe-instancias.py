class Estudante:
    escola = "DIO"

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
    
    def __str__(self):
        return f"{self.nome} - ({self.numero} - {self.escola})"

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

gui = Estudante("Guilherme", 1)
gi = Estudante("Giovanna", 2)

mostrar_valores(gui, gi)

print('\nAlterando Número')

gui.numero = 3

mostrar_valores(gui, gi)

print('\nAlterando escola')
Estudante.escola = "Alpha Lumen"
mostrar_valores(gui, gi)

print('\nCriando novo aluno')
aluno_3 = Estudante("Amanda", 4)
mostrar_valores(gui, gi, aluno_3)
