"""
Expressão condicional OR
"""

nome = input('Digite seu nome: ')
print(nome or 'Você não digitou nada')

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Matheus'

variavel = b or a or c or g or e or f or d or g
print(variavel)