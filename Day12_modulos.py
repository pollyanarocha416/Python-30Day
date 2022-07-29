# criar um modolo
# vc faz o escript e salva ele com .py
#exemplo:
#import Day12_ex_modulo as dem
#print(dem.generate_full_name('polly', 'rocha'))

#Usando o módulo python os é possível executar
#  automaticamente muitas tarefas do sistema operacional.
#import os
#os.mkdir('pastaTeste_moduloCriando_oMeu')


# função sys.argv retorna uma lista de argumentos de 
# linha de comando passados ​​para um script Python.
#import sys
#print('welcome {}. Enjoy {} challenge!'.format(sys.argv[1], sys.argv[2]))
#vc precisa chamar no terminal // py Day12_modulos.py Polly rocha


#modulos estatistico
from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3


#modulo string
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

from random import random, randint, ascii_letters
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
# gera um numero de 5 a 20
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive