"""
Format values with modifiers

: - To say a formatation was beginning

:s - Text(string)
:d - Integer(int)
:f - Numbers Float point (float)
:.(number)f - Amount decimal places (float)

:(character)(> OR < OR ^)(amount)(type - s, d or f)
> - left
< - right
^ - center
"""


num_1 = 10
num_2 = 3
num_3 = 94124
div = num_1 / num_2

print(f"\nTwo decimal places: {div:.2f}")
print(f"Ten places to left number '{num_2}': {num_2:0>10}")
print(f"Ten places to left number '{num_3}': {num_2:0>10}")

name = 'Matheus'
print(f"\nName normal: {name:s}")
print(f"\nName with # in both places, ie: {(50-len(name))/2} each place \n{name:#^50}")

last_name = 'Santos'
name_formatted = '\nName formatted: {n}'.format(n=name)
name_formatted2 = '\nName formatted: {0}{1:$^20}'.format(name, last_name)
print(name_formatted2)


print('\n\n')
name2 = 'Ana Carolina'
print(name2.lower())
print(name2.upper())
print(name2.title())
print(name2.ljust(50, '_'))
print(name2.rjust(50, '_'))
print(name2.center(50, '_'))