tupla_vazia = ()

#Create a tuple containing names of your sisters and 
# your brothers (imaginary siblings are fine)
tupla_brothers = ('Julia', 'Flavia', 'Paulo', 'Felipe')
tupla_sisters = tupla_brothers[0:2]
print(tupla_sisters)

#How many siblings do you have?
siblings_total = tupla_brothers + tupla_sisters
print(set(siblings_total))

#Modifique a tupla de irmãos e adicione o nome de seu pai 
# e sua mãe e atribua-o a family_members
tupla_family = ('mae', 'pai')
tupla_family += siblings_total
tupla_family = set(tupla_family)
tupla_family = sorted(tupla_family)
print(tupla_family)
del tupla_family[-1], tupla_family[-1]
tupla_family = tuple(tupla_family)
print(tupla_family)
