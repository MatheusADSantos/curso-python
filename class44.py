"""
Invertendo valores - class 44
"""

x = 10
y = 'Matheus'
z = 'Santos'
x,y,z = z, x, y
print(f'x={x}, y={y}, z={z}')

"""
Operação ternária - class 45
"""

logged_user = False
message = 'Usuário precisa logar' if logged_user else 'Usuário precisa logar'

idade = input('Qual sua idade')

if not idade.isnumeric():
    print('Você precisa digitar apenas número: ')
else:
    idade=int(idade)
    e_de_maior = idade >= 18
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar'

print(message)
print(msg)
