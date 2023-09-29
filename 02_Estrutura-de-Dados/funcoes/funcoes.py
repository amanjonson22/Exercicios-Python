def exibir_mensagem():
    print('Olá mundo!')

def exibir_mensagem_2(nome):
    print(f'Seja bem-vindo {nome}!')

def exibir_mensagem_3(nome = 'Anônimo'):
    print(f'Seja bem-vindo {nome}!')

exibir_mensagem()
exibir_mensagem_2(nome='Amanda')
exibir_mensagem_3()
exibir_mensagem_3(nome='Amanda')

#RETURN

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([10, 20, 34]))
print(retorna_antecessor_e_sucessor(10))

def func_3():
    print('Olá mundo!')

print(func_3()) #None

#ARGUMENTOS NOMEADOS
def salvar_carro(marca, modelo, ano, placa):
    print(f'Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}')

salvar_carro('Fiat', 'Palio', 1999, 'ETI-2146')
salvar_carro(marca='Fiat',modelo='Palio',ano=1999, placa='GFD-5341')
salvar_carro(**{"marca": 'Fiat', "modelo": 'Palio', "ano": 1999, "placa": "GFS-8764"})

#ARGS E KWARGS
def exibir_poema(data_extenso, *args, **kwargs):
    texto = '\n'.join(args)
    meta_dados = '\n'.join([f'{chave.title()}: {valor}' for chave, valor in kwargs.items()])
    mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    print(mensagem)

exibir_poema('Sex, 26 de agosto de 2022','Zen of Python', 'Beautiful is better than ugly.', autor ='Tim Peters', ano=1999)

#PARÂMETROS POR POSIÇÃO E KEYWORD
def criar_carro_2(modelo, ano, placa, /, marca, motor, combustível):
    print('\n',modelo, ano, placa, marca, motor, combustível)

criar_carro_2('Palio', 1999, 'ABC-1234',marca='Fiat', motor='1.0', combustível='Gasolina')

criar_carro_2('Palio', 1999,'ABC-1234', 'Fiat','1.0','Gasolina') #funciona também

def criar_carro_3(*,modelo, ano, placa, marca, motor, combustível):
    print('\n',modelo, ano, placa, marca, motor, combustível)

criar_carro_3(modelo='Palio', ano=1999, placa='ABC-1234',marca='Fiat', motor='1.0', combustível='Gasolina')

def criar_carro_4(modelo, ano, placa,/,*, marca, motor, combustível):
    print('\n',modelo, ano, placa, marca, motor, combustível)

criar_carro_4('Palio', 1999, 'ABC-1234', marca='Fiat', motor='1.0', combustível='Gasolina')

#OBJETOS DE PRIMEIRA CLASSE

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def test(a, b):
    return a * 2 + a * 3

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f'O resultado da operação é = {resultado}')

exibir_resultado(10, 10, somar)
exibir_resultado(12, 2, subtrair)
exibir_resultado(3, 5, test)

op = somar

print(op(1, 23))

#ESCOPO LOCAL E ESCOPO GLOBAL
salario = 2000

def salario_bonus(bonus, lista):
    global salario

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f'lista_aux = {lista_aux}')

    salario += bonus
    return salario

lista = [1]
print(salario_bonus(500, lista))
print('lista = ', lista)


