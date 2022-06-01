user = input('Enter with user: ')
length_characters = len(user)

if length_characters < 6:
    print(f'User must have at least 6 characters, not {len(user)}')
else:
    print('Registered')

# -------------------------------------------

'''
Method len() is used to count how many characters are in string
And for behind, the python, call method __len__() lets see in example
'''

print(len(user))
print(user.__len__())

