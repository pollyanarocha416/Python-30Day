#Duplas:

#Slicing tuples
from os import remove


tupla = ('Julia', 'felipe', 'Thiago', 'fernanda')
all_item = tupla[0:2]
print(all_item)

# Syntax
tpl = ('item1', 'item2', 'item3', 'item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)
print(middle_two_items)


#Changing Tuples to Lists
tuplaa= ('dfnl', 'kdfjask', 'wkfjasdkfj')
tuplaa = list(tuplaa)
print(tuplaa)

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
fruits[-1] = 'ultimo item'
#ordenado
fruits = sorted(fruits)
print(f"ordenado {fruits}")

del fruits[-1]
print(f"{fruits}\n")


fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')


#Checking an Item in a Tuple
tuplas_checking = ('item1', 'item2', 'item3')
print(f"estar ou nao? {'item5' in tuplas_checking}")
