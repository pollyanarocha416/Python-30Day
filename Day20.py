# pip e bibliotecas que podemos utilizar no dia a dia

import requests
import requests # importing the request module
import numpy
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
np_arr = numpy.array(lst)
print(np_arr)
qts_tem = len(np_arr)
print(qts_tem)

# esse modolo ja vem instalado no python

#import webbrowser

#url_list = ['http://www.python.org',
#            'https://www.linkedin.com/in/pollyana-rocha-3839a3216/',
#            'https://github.com/pollyanarocha416',
#    'https://twitter.com/Asabeneh',]
#for url in url_list:
#    webbrowser.open_new_tab(url)

#pra desintalar um pacote vc presisa execulta #pip unistall packagename
# pra lista pip list


# pra ler url pip request

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'  # text from a website

response = requests.get(url)  # opening a network and fetching a data
print(response)
print(response.status_code)  # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page


#lendo de uma api

url = 'https://restcountries.eu/rest/v2/all'  # countries api
response = requests.get(url)  # opening a network and fetching a data
print(response)  # response object
print(response.status_code)  # status code, success:200
countries = response.json()
# we sliced only the first country, remove the slicing to see all countries
print(countries[:1])
