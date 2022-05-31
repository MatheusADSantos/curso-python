"""
Input datas
"""

# name = input("Whats your name? ")
# age = input("How many years old? ")
# birth_year = 2022 - int(age)  # In this case I need to CAST str -> int

# print(f"User tapped {name} and \nYour variable type is {type(name)}")
# print(f'\n{name} has {age} years \nAnd your birth year is {birth_year}')

# -----------------------------------------------------
'''
How we can see, in method print, we need sum number_1 + number_2
But how can see, output of input ever be string, then we need to cast to int
If not, will concat theses 2 variables like: 2 + 2 => 22
'''
number_1 = int(input('\n\nTap a number '))
number_2 = int(input('Tap an other number '))

print(number_1 + number_2)
