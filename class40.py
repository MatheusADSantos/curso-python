"""
For / Else em Python
"""

variaveis = ['Matheus', 'Carol', 'Augusto']


print("Sem continue \nNeste caso mostro que não vai printar 2 x cada nome pois coloquei a palavra 'continue'")
for variavel in variaveis:
    print(variavel)
    print(variavel)

print('\nCom continue \nNeste caso vai imprimir uma unica ver cada print')
for variavel in variaveis:
    print(variavel)
    continue
    print(variavel)

print('\nCom break \nAqui após imprimir a primeira entra no break e para o loop')
for variavel in variaveis:
    print(variavel)
    break
    print(variavel)


print(f'\n\n{50 * "#"}')
comeca_com_w = False
# variaveis.append('Wellington')

# for variavel in variaveis:
#     if variavel.lower().startswith('w'):
#         comeca_com_w = True
#
#
# if comeca_com_w == True:
#     print(f'{variavel} Começa com W')
# else:
#     print('Não tem nenhum nome que começa com W')


for valor in variaveis:
    print(valor)
    if valor.lower().startswith('W'):
        break
else:
    print('Não tem nenhum nome que começa com W')

