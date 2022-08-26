#abri um arquivo txt e printar o que esta nele

#todo o texto
#f = open('./files/reading_file_example.txt')

f = open('C:/Users/Usuário/Desktop/txtArquivo/texto.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()


# Imprimindo alguns caracteres
fa = open('C:/Users/Usuário/Desktop/txtArquivo/texto.txt')
txts = fa.read(3)
print(type(txts))
print(txts)
fa.close()

#readline() : lê apenas a primeira linha
f = open('C:/Users/Usuário/Desktop/txtArquivo/texto.txt')
line = f.readline()
print(type(line))
print(line)
f.close()

#readlines() : lê todo o texto linha por linha e retorna uma lista de linhas
f = open('C:/Users/Usuário/Desktop/txtArquivo/texto.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()
#fechando o arquivos
with open('C:/Users/Usuário/Desktop/txtArquivo/texto.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)

with open('C:/Users/Usuário/Desktop/txtArquivo/texto.txt', 'a') as f:
    j = f.write('This text has to be appended at the end')
    print(j)


# Excluindo arquivos
# import os
# os.remove('./files/example.txt')




#Transformar um Json em um dicionario

import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print("----------------------------------------")
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

# ao contrario
# alterar um dicionário para um JSON, usamos o método dumps do módulo json.
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print("----------------------------------------")
print(type(person_json))
print(person_json)


#Salvando como arquivo JSON
# Também podemos salvar nossos dados como um arquivo json.
#  Vamos salvá-lo como um arquivo json usando as etapas a seguir.
#  Para escrever um arquivo json,
#  usamos o método json.dump(), que pode levar dicionário,
#  arquivo de saída, garantir_ascii e recuo.
#import json
# python dictionary
#person = {
#    "name": "Asabeneh",
#    "country": "Finland",
#    "city": "Helsinki",
#    "skills": ["JavaScrip", "React", "Python"]
#}
#with open('./files/json_example.json', 'w', encoding='utf-8') as f:
#    json.dump(person, f, ensure_ascii=False, indent=4)

print("-------------------------------------------")

# csv
#import csv
#with open('./files/csv_example.csv') as f:
#    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
#    line_count = 0
#    for row in csv_reader:
#        if line_count == 0:
#            print(f'Column names are :{", ".join(row)}')
#            line_count += 1
#        else:
#            print(
#                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
#            line_count += 1
#    print(f'Number of lines:  {line_count}')

#################################################

#Arquivo com extensão xlsx
#Para ler arquivos do Excel, precisamos instalar o pacote xlrd . Abordaremos isso depois de abordarmos a instalação de pacotes usando pip.

#excel_book = xlrd.open_workbook('sample.xls)
#print(excel_book.nsheets)
#print(excel_book.sheet_names)




# Pra ler arquivo xml

#import xml.etree.ElementTree as ET
#tree = ET.parse('./files/xml_example.xml')
#root = tree.getroot()
#print('Root tag:', root.tag)
#print('Attribute:', root.attrib)
#for child in root:
#    print('field: ', child.tag)


