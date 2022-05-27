""""
Begin with letter, can have numbers, seperate with underline(_), small letters
"""

name = 'Matheus Santos'
age = 31
height = 1.74
is_bigger = height > 18
weight = 110

print('Name: ', name)
print('Age: ', age)
print('Height: ', height)
print('Is Bigger: ', is_bigger)


imc = weight // (height ** 2)
print(name, 'have', age, 'years old and your IMC: ', imc)