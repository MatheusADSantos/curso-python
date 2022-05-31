name = 'Matheus Santos'
age = 31
height = 1.74
is_bigger = height > 18
weight = 110
imc = weight / (height ** 2)

print(name, 'have', age, 'years old and your IMC:', imc)
print(f'{name} have {age} years old and your IMC: {imc:.2f}')
print('{} have {} years old and your IMC: {:.2f}'.format(name, age, imc))
print('{1} have {0} years old and your IMC: {2:.2f}'.format(name, age, imc))  # To invert how to print this information


# ------------------------------------------------

name = 'Ana Carolina'
age = 22
height = 1.69
weight = 79
current_year = 2022
birth_year = current_year - age
imc = weight / (height ** 2)

print(f'\n\n{name} has {age} years and your birth-year is {birth_year} \nYour height is {height:.2f} and your IMC is {imc:.2f}')