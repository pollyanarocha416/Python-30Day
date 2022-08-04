# One way
language = 'Python'
lst = list(language)  # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst))  # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']


# gerar uma lista de números
# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
print(numbers)



#com if 

# Generating even numbers
# to generate even numbers list in range 0 to 21
even_numbers = [i for i in range(21) if i % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(even_numbers)

# Generating odd numbers
# to generate odd numbers in range 0 to 21
odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(positive_even_numbers)

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]


#lambda
# Named function
def add_two_nums(a, b):
    return a + b


print(add_two_nums(2, 3))     # 5
# Lets change the above function to a lambda function
def add_two_nums(a, b): return a + b


print(add_two_nums(2, 3))    # 5

# Self invoking lambda function
# 5 - need to encapsulate it in print() to see the result in the console
(lambda a, b: a + b)(2, 3)


def square(x): return x ** 2


print(square(3))    # 9
def cube(x): return x ** 3


print(cube(3))    # 27

# Multiple variables


def multiple_variable(a, b, c): return a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3))  # 22


#lambda dendro de outra funcao
def power(x):
    return lambda n: x ** n


# function power now need 2 arguments to run, in separate rounded brackets
cube = power(2)(3)
print(cube)          # 8
two_power_of_five = power(2)(5)
print(two_power_of_five)  # 32
