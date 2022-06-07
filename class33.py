"""
Management strings
- Indexes Strings
- Functions built-in len, abs, type, print, ...

Check:
https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/library/functions.html
"""
# positive [012345678]
# negative -[9876543210]
text = "Python_s2"
print(f'\nIndex 2 positive: {text[2]}')
print(f'\nIndex 2 negative: {text[-2]}')
print(f'\nIndex unitl 6 positive: {text[:6]}')
print(f'\nIndex 8 to 5 negative: {text[-8:5]}')
print(f'\nIndex 0 to 8 skip 2 by 2: {text[0::2]}')
print(f'\nIndex 1 to 8 skip 2 by 2: {text[1::2]}')
