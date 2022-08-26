#Escreva uma função que conte o número de linhas e
#  o número de palavras em um texto. 

# Todos os arquivos estão na pasta de dados: 

# a) Ler o arquivo obama_speech.txt e contar o número de linhas e palavras 
#readlines() : lê todo o texto linha por linha e retorna uma lista de linhas
f = open('C:/Users/Usuário/Desktop/txtArquivo/texto.txt')
# txt = f.read()
print("-------------------------------------------------")
nomes = f.readlines()

for nome in nomes:
    print(nome)

print("Número de linhas: ", len(nomes))
f.close()
print("-------------------------------------------------")
palavras = len(nome)
print(f"n de palavras: {palavras}")
# b) Ler o arquivo michelle_obama_speech.txt e contar o número de linhas e palavras 


# c) Ler o arquivo donald_speech.txt e contar o número de linhas e palavras 


# d) Leia o arquivo melina_trump_speech.txt e conte o número de linhas e palavras
