class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    @classmethod
    def criar_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2023 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

#p = Pessoa("Amanda", 20)
#print(p.nome, p.idade)

p2 = Pessoa.criar_data_nascimento(2002, 10, 22, "Amanda")
print(p2.nome, p2.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(10))