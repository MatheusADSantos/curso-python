"""
Listas em Python
Fatiamento
append, insert, pop, del, clear, extend, +
main, max
range
"""

#         0    1      2       3    4    5    6
lista = ['A', 'B', 'PYTHON', 'C', 'D', 10.5, 'E']
#        -7   -6     -5      -4   -3   -2    -1

print(lista[0:])
print(lista[1:5])
print(lista[2:])
print(lista[-1:])
print(lista[-7:])

print(f'\n\n{50 * "#"}')
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = []

l3.extend(l1)
l3.extend(l2)
print(f'Lista 3 extendida da lista 1 e 2 \n{l3}\n')

l3.append('b')  # Joga no final da lista
print(f'Lista 3 agora add "b" no final da lista com append() \n{l3}\n')

l3.insert(3, 'python is fuck...')  # Estou inserindo no indice 0(inicio da lista)
print(f"Agora a lista 3 com 'python is fuck' no indice 3 da lista: \n{l3}\n")

l3.pop()
print(f"Agora dando um pop() removendo o utilmo item da lista: \n{l3}\n")

del (l3[3])
print(f"Agora dando um del() no indice 3: \n{l3}\n")

print(f'\n\n{50 * "#"}')

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

soma = 0
for valor in lista:
    soma += valor
print(soma)

print(f'\n\n{50 * "#"}')

tipos = ['String', True, 10, -43.2]

for tipo in tipos:
    print(f"\n'{tipo}' é do tipo: \n{type(tipo)}")

print(f'\n\n{50 * "#"}')

secreto = 'python'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('\n\nVocê perdeu!!!')
        break

    letra = input('\nDigite uma letra: ')
    if len(letra) > 1:
        print('Ahhh isso não vale \nDigite apenas uma letra')
        continue
    digitadas.append(letra)

    if letra in secreto:
        print(f'Uhuuul a letra {letra} existe na palavra secreta')
    else:
        print(f"Afff a letra '{letra} não existe na palavra seccreta'")
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'\nVocê ainda tem {chances} chances... ')
