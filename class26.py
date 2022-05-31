"""
Logic Operation

and, or, not
in, not in
"""

a = 2
b = 2
c = 5

comparation1 = a == b  # True
comparation2 = a < c   # True
comparation3 = a != b  # False

# Logic AND (Whenever all conditions are True)
if comparation1 and comparation2:
    print(f'\n\nLogic AND (Whenever all conditions are True):\n{comparation1} and {comparation2} => {comparation1 and comparation2}')

# Logic OR (Whenever at least one are True)
if comparation1 or comparation3:
    print(f'\n\nLogic OR (Whenever at least one are True):\n{comparation1} or {comparation3} => {comparation1 or comparation3}')

# Logic NOT (Invert logic boolean)
if not(not comparation1):  # Denial of denial
    print(f'\n\nLogic NOT (Invert logic boolean):\n not {comparation1} => {not comparation1}')

# -----------------------------------------

name = 'Matheus Augusto'
search = input("\n\nWhat are you searching? ")
if search in name:
    print(f'{name} has string {search}')
else:
    print(f'Not exist {search} in {name}')

# -----------------------------------------


user = input("\n\nUser Name: ")
password = input("Password: ")

db_user = 'Matheus'
db_password = '123456'

if user == db_user and password == db_password:
    print(f'Login Success!!!')
else:
    print(f'User or Password invalid... :X')
