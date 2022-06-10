# Índices
# 0123456789.................33

frase = 'o rato roeu a roupa do rei de roma'  # Valor Iterável, que é possível percorrer...
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_usuario = input('Qual letra quer colocar em maiusculo? ')
while contador < tamanho_frase:
    # print(frase[contador], contador)

    # nova_string += frase[contador]
    # print(nova_string)

    letra = frase[contador]
    if letra == input_usuario:
        nova_string += input_usuario.upper()
    else:
        nova_string += letra
    contador += 1
print(f'\n{nova_string}')


