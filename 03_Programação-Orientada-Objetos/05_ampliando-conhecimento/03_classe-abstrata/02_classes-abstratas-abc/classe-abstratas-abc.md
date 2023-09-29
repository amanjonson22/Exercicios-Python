# Criando classes abstratas com o módulo abc

## Sigla ABC

Significa Abstracted Base Class. É um módulo do Python para criar classes abstratas.

O ABC funciona decorando métodos da classe base como abstratos e, em seguida, registrando classes concretas como implementações da base abstrata. Um método se torna abstrato quando decorado com `@abstractmethod`.

O `@abstractmethod` força a classe filha implementar em seu corpo os métodos abstratos da classe pai, fazendo com que a mesma siga o padrão. Isso auxilia na utilização do polimorfismo.

## Prática

Código prático:

- [01_classes-abstratas.py](01_classes-abstratas.py)