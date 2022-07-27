"""
Validando CPF
CPF = 168.995.350-09
"""

cpf = input('Digite seu cpf: ')
# cpf = '16899535009'
# cpf = '37138215851'
novo_cpf = cpf[:-2]  # Removendo os dois ultimos digitos


soma_das_multiplicacao = 0
for index, const in enumerate(range(10, 1, -1)):
    # print(f'Constate: {const}, Número do Novo CPF no indice {index}: {novo_cpf[index]}')
    numero_do_cpf = int(novo_cpf[index])
    multiplicacao = numero_do_cpf*int(const)
    soma_das_multiplicacao += multiplicacao
print(soma_das_multiplicacao)

dig = 11 - (soma_das_multiplicacao%11)
dig_1 = 0 if (11 - (soma_das_multiplicacao%11) > 9) else dig
print(f'Dig1: {dig_1}')

soma_das_multiplicacao = 0
novo_cpf_dig1 = novo_cpf + str(dig_1)
for index, const in enumerate(range(11, 2, -1)):
    numero_do_cpf = int(novo_cpf_dig1[index])
    multiplicacao = numero_do_cpf*int(const)
    soma_das_multiplicacao += multiplicacao
print(soma_das_multiplicacao)

dig = 11 - (soma_das_multiplicacao%11)
dig_2 = str(dig)
dig_2 = dig_2[:1]
print(f'Dig2: {dig_2}')

CPF = novo_cpf + '-' + str(dig_1) + dig_2
print(f'\n\nPortando seu CPF é {CPF}')