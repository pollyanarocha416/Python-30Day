#funcao com um valor retorno
from functools import reduce


def square(x):          # a square function
    return x ** 2


def cube(x):            # a cube function
    return x ** 3


def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)


def higher_order_function(type):  # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute


result = higher_order_function('square')
print(result(30))       # 9
result = higher_order_function('cube')
print(result(2))       # 27
result = higher_order_function('absolute')


#Python permite que uma função aninhada acesse o escopo 
# externo da função delimitadora.
def add_ten():
    ten = 10

    def add(num):
        return num + ten
    return add
closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20


#Decoradores Python
#Um decorador é um padrão de design em Python
#  que permite ao usuário adicionar novas funcionalidades
#  a um objeto existente sem modificar sua estrutura.
# Normal function
def greeting():
    return 'Welcome to Python'


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper


g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON


#aplicando varios decoradores 

'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator# order with decorators is important in this case - .upper() function does not work with lists
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

#Aceitando Parâmetros em Funções do Decorador
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')


#Funções de ordem superior incorporadas: lambda
numbers = [1, 2, 3, 4, 5]  # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x: x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

#exemplo 2
numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]

#exemplo 3
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
def change_to_upper(name):
    return name.upper()
names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
# Let us apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']



#funcao filtro
# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable
def is_even(num):
    if num % 2 == 0:
        return True
    return False
even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]

numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)
total = reduce(add_two_nums, numbers_str)
print(total)    # 15
