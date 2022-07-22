#Escape Sequences in Strings
#\n: new line
#\t: Tab means(8 spaces)
#\\: Back slash
#\': Single quote (')
#\": Double quote (")
print('line break')
print('Day four \t 4')# o t pula 8 de espaço
print('i dont know \t\t3')


#string formatting
#'''
# %s - String (or any object with a string representation, like numbers) 
# %d - Integers 
# %f - Floating point numbers 
# "%.number of digitsf" - Floating point numbers with fixed precision '''

# Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' % (first_name, last_name, language)
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' % (
    radius, area)  # 2 refers the 2 significant digits after the point
print(formated_string)


python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
# "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"
print(formated_string)

k = 6
j = 4.5
l = 6
print(f'k * j + l = {k - j + l:2f}')

a = 4
b = 3.5
print(f'{a} / {b} = {a / b:.2f}')


greeting = 'hello word'

print(greeting[-1:5:-1])
#::stap >> reverse
#start:
#:stop: >> onde vai parar

#string metodos String Methods

#.capitalize() >> escrever com letra maiuscula

#count(): returns occurrences of substring in string, 
# count(substring, start=.., end=..).
challenge = 'thirty days of python'
print(challenge.count('y', 7, 14))  # 1,

#endswith(): Verifica se uma string termina com um final especificado
challenge = 'thirty days of python'
print(challenge.endswith('python'))   # True
print(challenge.endswith('aaaa'))  # False

#.expandtabs() substitue por espaço a tabulacao \
#find() retorna a primeira ocorrencia da quilo q vc passou como parametro se nao -1
#rfind() retorna a ultima
#index() retorna o q tu passo como parametro o inicio
#rindex() retorna o q tu passo como parametro o fim

#isalnum(): Checks alphanumeric character
challenge = '30DaysPython'
print(challenge.isalnum())  # True

challenge = 'thirty days of python'
print(challenge.isalnum())  # False, space is not an alphanumeric character

#isalpha(): Verifica se todos os elementos da string são caracteres alfabéticos (a-z e A-Z)
#isdecimal(): Verifica se todos os caracteres em uma string são decimais (0-9)

#isdigit(): Verifica se todos os caracteres em uma string são números (0-9 e alguns outros caracteres unicode para números)
challenge = '\u00B2'
print(challenge.isdigit())   # True

#isidentifier(): Verifica se há um identificador válido - verifica se uma string é um nome de variável válido
challenge = 'thirty days of python'
print(challenge.islower())  # True
challenge = 'Thirty days of python'
print(challenge.islower())  # False

#join(): Retorna uma string concatenada
lista = ['polly', '20', 'software enginner']
concatenar = ' '.join(lista)  # polly 20 software enginnir
print(concatenar)

#split(): divide a string, usando uma determinada string ou espaço como separador
challenge = 'thirtydaysofpython'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

#swapcase(): >> caixa de troca():  Tt tT
#startswith(): Verifica se a string inicia com a string especificada
