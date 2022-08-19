#data e hora em Python
from datetime import date
from datetime import datetime
#import datetime

#listar os comandos de data e hora
#print(dir(datetime))

now = datetime.now()
print(now)                      # 2021-07-08 07:34:46.549883
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38


#Formatação de data e hora usando o método strftime

# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)
months = datetime.now()
month1 = months.strftime("%d/%m/%Y")
print(month1)


#separado por -
d = date(2020, 1, 1)
print(d)
print('Current date:', d.today())    # 2019-12-05
# date object of today's date
today = date.today()
print("Current year:", today.year)   # 2019
print("Current month:", today.month)  # 12
print("Current day:", today.day)     # 5

#erro e execoes
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2022 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')


def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e
lst = [1, 2, 3, 4, 5]
# TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
print(sum_of_five_nums(lst))

#maneira serta de fazer
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e
lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15


#Também podemos usar a 
# descompactação na função interna de 
# intervalo que espera um início e um fim.

numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers))  # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)      # [2, 3, 4, 5,6]


#Às vezes, gostaríamos de combinar listas ao percorrê-las. Veja o exemplo abaixo:
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit': f, 'veg': v})

print(fruits_and_veges)
