"""
Desempacotamento de lsitas
"""

lista = ['Matheus', 'Ana Carolina', 'Marcela', 1, 2, 3, ..., 1000]

# n1, n2, n3 = lista


# n1, n2, *outra_lista, ultimo_da_lista = lista
# print(n1, n2, outra_lista)
# print(outra_lista)
# print(ultimo_da_lista)


n1, n2, *_ = lista  # Neste caso, o que me importa somente os dois primeiros valores da lista
print(n1, n2)