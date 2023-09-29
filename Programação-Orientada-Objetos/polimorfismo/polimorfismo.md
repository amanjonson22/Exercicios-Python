# POLIMORFISMO

## Aula 
### Objetivo - Aprender a criar classes polimórficas.
- Etapa 1 - O que é?
- Etapa 2 - Polimorfismo com herança

## O que é?

Polimorfismo significa algo que tem muitas formas. Na programação é ter algo que tem um nome, porém quando passa um número, o objeto se comporta de uma forma, quando passa uma string, funciona mas se comporta de outra forma.
Capacidade de trabalhar tendo o mesmo nome, mas com comportamentos diferentes.

Exemplos:
```
len("python")
len([10, 20, 30])
```
Para cada objeto, o len se comporta de uma forma.

## Polimorfismo com herança
É o mesmo método com comportamentos diferentes.
É útil nos casos em que o método herdado da classe pai não se encaixa perfeitamente na classe filho.

|Classe Animal|
|-------------|
|Pássaro é um animal, assim como o cachorro, porém um voa e o outro anda|

```
class Passaro:
    def voar(self): pass

class Pardal(Passaro): 
    def voar(self):
        print("Pardal voa")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

def plano_de_voo(passaro):
    passaro.voar()

plano_de_voo(Pardal())
plano_de_voo(Avestruz())
```
Na implementação do voar do avestruz, o método `voar` irá printar "Avestruz não voa". 
No polimorfismo, um método ou função recebe um atributo e vai chamar um nome, que, no caso, está sendo representado por voar.

Onde está funcionando o polimorfismo no código:
```
def plano_de_voo(passaro):
    passaro.voar()

plano_de_voo(Pardal())
plano_de_voo(Avestruz())
``` 
Ou seja, quando passa `Pardal()`, irá mostar: `Pardal voa`. Quando passa `Avestruz()`, irá mostrar: `Avestruz não voa`.

- [Prática do código](\01_polimorfismo.py)

Todo objeto que for aplicar o polimorfismo, precisa do método em todas as classes filhas, porém com resultados diferentes. No caso dos pássaros, todas as aves tinham o método `voar`, porém, tinham resultados diferentes.