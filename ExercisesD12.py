import string
import random

#number_of_strings = 1
#length_of_string = 6
#for x in range(number_of_strings):
#  print(''.join(random.choice(string.ascii_letters + string.digits)
#        for _ in range(length_of_string)))

#gerar id aleatorio
def gerar_id():
    qts_ids = 1
    comprimento_do_id = 6
    for x in range(qts_ids):
        print(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(comprimento_do_id)))
gerar_id()

#gerar id apartir do que o user quer
def user_id_gen_by_user():
    qts_id = int(input("qtdd "))
    comprimento_id = int(input("compr "))
    for x in range(qts_id):
        print(''.join(random.choice(string.ascii_letters + string.digits)
              for _ in range(comprimento_id)))
user_id_gen_by_user()


from random import random, randint
#Escreva uma função chamada rgb_color_gen.
#  Ele irá gerar cores RGB (3 valores variando de 0 a 255 cada).
def rgb_color_gen():
    a = randint(100, 900)
    b = randint(100, 900)
    c = randint(100, 900)
    return f"rgb({a},{b},{c})"
print(rgb_color_gen())    