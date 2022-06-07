"""
While in Python
And learn run in debug with breack point...
"""

# condition = True
# while condition:  # loop infinity
#     name = input('Whats UR name? ')
#     print(f'Hi {name}')
# print('Never execute ...')

# ---------------------------------------------

# x = 0
# while x < 5:
#     print(f'X: {x}')
#     x = x + 1
# print('Finish loop')

# ---------------------------------------------

# x = 0
# while x < 10:
#     if x == 3:
#         x = x + 1
#         # continue
#         break
#     print(f'X: {x}')
#     x = x + 1
#
# print('Finish loop')

# ---------------------------------------------

# x = 0  # column
# while x < 10:
#     y = 0  # row
#     while y < 5:
#         print(f'X,Y({x},{y})')
#         y = y +1
#     x += 1  # x = x + 1
# print('Finish loop')

# ---------------------------------------------

while True:
    print()
    num_1 = input('Tap a number: ')
    num_2 = input('Tap other number: ')
    operation = input('Tap Operation: ')
    exit = input('Wish exit? (y/n) ')

    if exit == 'y':
        break

    if not num_1.isnumeric() and num_2.isnumeric():
        print('Tap a number...')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operation == '+':
        print(num_1 + num_2)
    if operation == '-':
        print(num_1 - num_2)
    if operation == '*':
        print(num_1 * num_2)
    if operation == '/':
        print(num_1 / num_2)
