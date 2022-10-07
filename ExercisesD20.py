# as 10 palavras mais comuns de romeu e julieta
import requests
import collections

romeo_and_juliet = ' http://www.gutenberg.org/files/1112/1112.txt '
response = requests.get(romeo_and_juliet)
c = collections.Counter(romeo_and_juliet)
print(c)
c.most_common(10)





# exemplo

# Lista de palavras
words = ['Banana', 'Maçã', 'Laranja',
         'Melão', 'Uva', 'Abacaxi', 'Abacate', 'Pimenta', 'Banana',
         'Maçã', 'Banana', 'Melão', 'Banana', 'Uva', 'Abacaxi', 'Fake', 'Fake']

# Contador para as ocorrencias de cada palavra
c = collections.Counter(words)
print(c)
c.most_common(10)
