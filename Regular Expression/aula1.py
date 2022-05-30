# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto

import re

''' 
Functions by re: 
findall/search/sub/compile

Test is different form test
'''

string = 'This a test from regular expression, to test some functions in Regex with Python 3'
print(re.search(r'test', string))
print(re.findall(r'test', string))
print(re.sub(r'test', 'example', string, count=1))  # Default is 0 when sub all occurencies

regexp = re.compile(r'test')  # To reutilize function regex
print('\n\n', regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('another exemple', string, count=1))