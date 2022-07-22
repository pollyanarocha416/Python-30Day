from posixpath import split


lista = ['Lica', 'K1', 'K2', 'Elem', 'Bene', 'Tina', 'Keila']
listas = len(lista)
#print(listas)

#Obter o primeiro item, o item do meio e o último item da lista
Prilist = lista[0]
meioList = lista[3]
ultList = lista[-1]
#print(Prilist)
#print(meioList)
#print(ultList)

#Declare uma lista chamada mixed_data_types, 
# coloque seu(nome, idade, altura, estado civil, endereço)
mixed_data_types = ['polly', 20, 1.60, 'solteira', 'rua x n2233']
p1 = mixed_data_types[0]
#print(p1)
pMeio = mixed_data_types[2]
#print(pMeio)


#meio arredondar o valor round()
def data_types(itens):
    dividir = len(itens) / 2
    meio = round(dividir)
    meios = itens.index(int(meio))
    for meios in itens:
        return meios

valor = data_types(['Lica', 'K1', 'K2', 'Elem', 'Bene', 'Tina', 'Keila'])
print(valor)