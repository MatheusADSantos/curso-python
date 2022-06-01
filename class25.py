"""
https://docs.python.org/3/library/stdtypes.html
Logic Operations

< - strictly less than
<= - less than or equal
> - strictly greater than
>= - greater than or equal
== - equal
!= - not equal
is - object identity
is not - negated object identity

"""

number_1 = 2  # int
number_2 = 2  # int

expression = (number_1 == number_2)
if expression:
    print(f"Expression is {expression}")

# ----------------------------------------------
var_1 = 'Matheus'
var_2 = 'Ana'

expression_2 = (var_1 != var_2)
if expression_2:
    print(f"\nVar1 is different from Var2? \n{expression_2}")

# ----------------------------------------------

name = input('\n\nWhat is your name? ')
age = input('How old are you? ')
age = int(age)  # Casting string from input to integer

# Limit to get lending
smaller_age = 25
bigger_age = 40

if age >= smaller_age and age <= bigger_age:
    print(f'{name} can get lending...')
else:
    print(f"{name} don't can to get lending ... :/")
