"""
For in python
Iterando strings com for
Funcão range(start=0, stop, step=1)
"""

texto = 'Python'

for letra in texto:
    print(letra)


print(f'\n{30 * "#"}')
for n in range(0, 50, 3):  # Começa no 0 e vai até 50 pulando de 3 em 3
    print(f'{n}')



print(f'\n{30 * "#"}')
primos_8 = []
for x in range(100):
    if x % 8 == 0 and x != (0):  # Aqui estou achando os multiplos de 8... Se o resto da div de x/8 é igual a 0
        primos_8.append(x)
        print(f'{primos_8}')
print(f'\nPortanto os números multiplos de 8 nun range de 0 à 100 é: \n{primos_8}')



print(f'\n{30 * "#"}')
texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)