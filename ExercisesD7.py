from audioop import add


it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Encontre o comprimento do conjunto it_companies
print(len(it_companies))

#  Adicionar 'Twitter' a it_companies
it_companies.add('Twitter')
print(it_companies)
#  Insira várias empresas de TI de uma só vez no conjunto it_companies
it_companies.update(['aaaaa', 'hgfghf', 'jhjghjhg'])
print(it_companies)
#  Remova uma das empresas do conjunto it_companies
it_companies.pop()
print(it_companies)
#  Qual é a diferença entre remover e descartar
