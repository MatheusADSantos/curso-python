"""
Create a function1 that receive like parameter the return from function2 and return your return
"""


def func1(parameter):
    return parameter


def func2():
    return print('Return from func2 called from func1')


func1(func2())

"""
Create a function1 that receive a function2 like parameter and return the value from function2 executed
Do function1 execute two functions that receive a different number of arguments
"""


def main_function(function, *args, **kwargs):
    return function(*args, **kwargs)


def say_hi(name):
    return f'Hi {name}'


def ask_question(name, question):
    return f'{name}, {question}'


execute = main_function(say_hi, 'Matheus')
execute2 = main_function(ask_question, 'Matheus', question='Where are you from?')
# print(execute)
print(execute2)

# *args(Arguments) are arguments to implicit like a parameter in function to use when the function has
# **kwarg(Keywords Argument) are same args, but named to use like a parameter in a function
