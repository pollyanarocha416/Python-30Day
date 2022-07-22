lst = ['item', 'item2', 'item3', 'item4', 'item5']

# o rest vai acabar recebendo o valor q sobrar
first_item, second_item, third_item, * rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

#outros exemplos 
# Second Example about unpacking list
first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
# Third Example about unpacking list
countries = ['Germany', 'France', 'Belgium', 'Sweden',
             'Denmark', 'Finland', 'Norway', 'Iceland', 'Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

# mexer com lista tem .remove(''), .incert(0, ' '), .appendACRECENTAR(' ')
#.pop() REMOVE O ULTIMO ITEM DA LISTA, del fruits[0] >> passo como parametro
# a possisao do item q eu quero exluir, O método clear() esvazia a lista:

#anexar uma lista na outra
negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
# Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
print('Integers:', negative_numbers)

#Var.count(' ')

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, the first occurrence

#O método reverse() inverte a ordem de uma lista.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)  # ['lemon', 'mango', 'orange', 'banana']

#sort
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
# sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
print(fruits)
fruits.sort(reverse=True)
print(fruits)  # ['orange', 'mango', 'lemon', 'banana']
