#filtrar negativos
numbers = [-5,-4, -3, -2, -1, 0, 2, 4, 6]
negative_numbers = [i for i in numbers if i % 2 != 0 or i % 2 == 0 and i < 0]
print(negative_numbers)

#Achate a seguinte lista de listas de listas para uma lista unidimensional:
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
achatar = [number for row in list_of_lists for number in row]
print(achatar)
achatar2 = [n for row2 in achatar for n in row2]
print(achatar2)