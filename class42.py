"""
Enumerate - Enumerar elementos da lista
"""

lista = [
    # 0    1    2
    ['A', 'B', 'C'],  # 0
    ['D', 'E', 'F'],  # 1
    ['G', 'H', 'I'],  # 2
]

# print(lista[1][2])
enumerada = list(enumerate(lista))  # Convertemos para uma lista com um cast
print(enumerada[0][1])
print(enumerada[1][1])
print(enumerada[2][1])

print('\n')
for indice, valores in enumerada:
    print(indice, valores)