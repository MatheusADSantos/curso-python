'''
Documentations and functions built-in utils
https://docs.python.org/3/library/stdtypes.html

We have 3 situations:
- Without deals
- With extensions functions personal to trate
- With try except
'''

# num1 = input('Type a number: ')
# num2 = input('Type another number: ')
#
# # isnumeric(Number Positives) isdigit isdecimal
# print(num1.isnumeric())
# print(num2.isnumeric())
#
# if num1.isdigit() and num2.isdigit():
#     num1 = int(num1)
#     num2 = int(num2)
#
#     print(num1 + num2)

# ----------------------------------------------


import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


###########
#  USAGE  #
###########

# Float
print(is_float('-101.0112'))  # True
# Int
print(is_int('-1010112'))  # True
# Numbers in general (float ou int)
print(is_number('-1010.112'))  # True
# False
print(is_number('123a'))  # False


# num1 = input('Type a number: ')
# num2 = input('Type another number: ')
#
# if is_number(num1) and is_number(num2):
#     num1 = float(num1)
#     num2 = float(num2)
#
#     print(num1 + num2)
# else:
#     print('Error')


# -------------------------------------------------------------

num1 = input('Type a number: ')
num2 = input('Type another number: ')

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('Error')