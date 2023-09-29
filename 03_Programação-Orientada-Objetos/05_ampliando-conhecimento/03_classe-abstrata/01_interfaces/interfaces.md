# Interfaces

### O que são interfaces?

Interfaces definem o que uma classe deve fazer e não como.

Uma interface é uma forma de que quando todo mundo quer implementar algo, seguem aquele padrão.

Exemplo.: A interface de uma lapiseira é que tem que ter um grafite e um botão para apertas e o grafite desça. Independente do design, a interface da lapiseira é essa.

Assim, consegue garantir n versões de algo, porém, sempre seguindo o mesmo padrão.

### Python tem interface?

O conceito de interface é definir um contrato, onde são declarados os métodos (o que deve ser feito) e suas respectivas assinaturas. Em Python utilizamos classes abstratas para criar contratos. Classes abstratas não podem ser instanciadas.

Então, o Python não tem uma palavra reservada `interface`, para conseguir construir um contrato, utiliza o conceito de classe abstrata e extende quantas classes forem necessárias.

Classes abstratas não devem e não podem ser instanciadas.