""""
Crie uma funcao que exibe uma saudacao com os parâmetros saudacao e nome
"""

def saudacao(saudacao, nome):
    print(saudacao, nome)

saudacao('Olá', 'Matheus')


""""
Crie uma funcao que receba 3 numeros como parâmetro e exiba a soma entre eles
"""

def soma(numero1, numero2, numero3):
    numero1 = (type(numero1) == float and float(numero1) or int(numero1))
    numero2 = float(numero2)
    numero3 = float(numero3)
    resultado = numero1 + numero2 + numero3
    # resultado = int(resultado)
    print(f'\nNúmero1: {numero1} é do tipo: {type(numero1)} Float: {type(numero1) == float} Int: {type(numero1) == int}')
    print(f'Número2: {numero2} é do tipo: {type(numero2)} Float: {type(numero2) == float} Int: {type(numero2) == int}')
    print(f'Número3: {numero3} é do tipo: {type(numero3)} Float: {type(numero3) == float} Int: {type(numero3) == int}')
    print(f'A soma dos 3 números é {resultado}')

n1 = input('Entre com número 1: ')
n2 = input('Entre com número 2: ')
n3 = input('Entre com número 3: ')
soma(n1, n2, n3)


"""
Crie uma funcao que receba 2 números. O primeiro é um valor o segundo um percentual (Ex: 10%)
Retorne return o valor do primeiro numero somado do aumento do percentual do mesmo
"""

def percentualDe(valor, percentual):
    valor_aumentado = float(valor) * (1 + (float(percentual)/100))
    return print(f'Valor Aumentado: {valor_aumentado}')

valor = input('\n\nValor: ')
porcentagem = input('Porcentagem: ')

percentualDe(valor, porcentagem)



""""
Fizz Buzz - Se o parâmetro da função for divisivel por 3, retorne 3,
Se o parâmetro da função for divisivel por 5, retorne Buzz
Se for divisivel pelos 2, retorne FizzBuzz
Se não retorne, número inválido!
"""

def fizzBuzz(parametro):
    valor = float(parametro)
    fizz = (valor % 3) == 0
    buzz = (valor % 5) == 0
    if fizz and buzz:
        return print('\n\nFizz')
    elif (buzz):
        return print('\n\nBuzz')
    elif (fizz):
        print('\n\nFizzBuzz')
    else:
        return print('\n\nNúmero Inválido')

fizzBuzz(15)