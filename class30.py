"""
Situation: Ask to user to tap a number integer and let he know if that number is even or odd
Otherwise, inform he and try again ...
"""


def check_number(number):
    if number.isdigit():
        print(f'{number} is a number')
        number = int(number)
        if (number % 2) == 0:
            print(f'{number} is EVEN')
        else:
            print(f'{number} is ODD')
    else:
        print(f'Not is a number \nPlease try again')
        x = input('\nEnter a number integer: ')
        check_number(x)  # Here I'm using recursion function


# -------------------------------------------------------------
"""
Situation2: Ask to user to say what time is it...
Then print hello, (greet) according the hour
"""


def greets(clock):
    if clock.isdigit():
        clock = int(clock)
        if clock > 0 and clock < 23:
            print("Value is alright to continue....")

            if 0 < clock < 11:
                print(f"Now its {clock} \nThen Goog Morning...")
            elif 12 <= clock < 17:
                print(f"Now its {clock} \nThen Goog Afternoon...")
            else:
                print(f"Now its {clock} \nThen Goog Evening...")
        else:
            x = input("Please, enter a time o clock correctly (0h -> 23h): ")
            greets(x)  # Here I'm using recursion function
    else:
        x = input("Please, enter a time o clock correctly (Only number integer): ")
        greets(x)  # Here I'm using recursion function


# -------------------------------------------------------------

"""
Ask to user to tap your name
Then check length name and say if is normal/short or langer
"""


def check_length_name(name):
    if name.isalpha():
        print(f"{name} is alphabetic and has {len(name)} characters! \nThen can continue...\n")
        if len(name) < 4:
            print(f"-> You name is too short")
        elif len(name) > 6:
            print(f"-> Your name is too long")
        else:
            print(f"-> Your name is normal")
    else:
        name = input('\nPlease, check if you tap correct name \nWith only characters ... \nName: ')
        check_length_name(name)  # Here I'm using recursion function


# -------------------------------------------------------------

# name = input("\nHey what's your name? ")
# check_length_name(name)

# clock = input('\nHi! \nWhats time is it? ')
# greets(clock)

# number = input('\nEnter a number integer: ')
# check_number(number)
