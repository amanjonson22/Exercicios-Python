# Atributos de Classe e Instância

**Foco:** variáveis de classe e variáveis de instância.

**Objetivo Geral:** Entender as diferenças entre as variáveis de classe e variáveis de instância.

## Etapas

- **Etapa única:** O que são e como utiliza.

### Atributos do objeto

Todos os objetos nascem com o mesmo número de atributos de classe e de instância.

*Atributos de instância:* Diferentes para cada objeto.

*Atributos de classe:* Compartilhados entre objetos.

Exemplo:
```
class Estudante:
    escola = "DIO"

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
    
    def __str__(self):
        return f"{self.nome} - ({self.numero} - {self.escola})"

gui = Estudante("Guilherme", 56451)
gi = Estudante("Giovanna", 17323) 
```

### O que é de classe e o que é de instância?

Toda variável de classe está declarada após da definição da classe. Nesse caso é `escola = "DIO"`. Esse atributo é compartilhado entre as variáveis `gui` e `gi`.

- [Prática](01_atributos-classe-instancias.py)

**Atributo de instância é único para cada objeto.**

Ou seja, se alterar um item de uma variável, não deve alterar em outra variável. Neste exemplo, o `numero` da variável `gui`, caso alterado, não irá modificar o `numero` da variável `gi`.

*É individual para cada objeto.*

Sabemos que é de instância quando declarada no `def __init__`:
```
self.instância
```

**Atributo de classe é da classe.**

Se alterar o atributo da classe, irá alterar em todas as variáveis criadas seguintes. Neste exemplo, `escola`, quando modificado, irá alterar tanto em `gui` quanto em `gi`.

Ele muda para todas as instâncias criadas.

*É única para todos os objetos.*