st = {'item1', 'item2', 'item3', 'item4'}
st.add('aaaa')
#st.update(['item5', 'item6', 'item7'])

#{'item5', 'item6', 'item3', 'item1', 'aaaa', 'item7', 'item4', 'item2'}
print(st)
#ad(), frutas.pop() # remove um item aleatório do conjunto, st.clear() 
# > limpar td a set print(fruits) # set(), st3 = st1.union(st2)

conjunto = {'a', 'b', 'c', 'd'}
uniao = st.union(conjunto)#cria um novo conjunto
print(uniao)

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2', 'ffawwaef', 'faweadf', 'item1'}
st3 = st1.intersection(st2)  # {'item3', 'item2'}
print(st3)

#super conjunto do outro
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers)  # False, because it is a super set
whole_numbers.issuperset(even_numbers)  # True

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.issubset(dragon)     # False

#.difference(),
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers)  # {0, 6, 7, 8, 9, 10}

#se e conjunto ou disjunto
even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers)  # True, because no common item

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}
