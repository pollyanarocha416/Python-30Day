from re import A


def add_two_numbers(a, b):
    return a + b
print(add_two_numbers(5, 5))


#printar A área de um Círculo é pi vezes o raio elevado ao quadrado 
def circulo(r):
    pi = 3.14
    a = pi * r ** 2
    return a
print(circulo(1))

#soma qualquer valor passado
def add_all(*every_thing):
    total = 0
    for i in every_thing:
        total += i
    return total
print(add_all(4, 9, 6, 4))

#converter Celsius para fahrenheit
def conveter(c):
    f = c * 9 / 5 + 32
    return f
print(conveter(4))    

#dito o mes ele retorna a estacao do ano
def estacao_do_tempo(mes):
    estacoes = ['primavera', 'verao', 'inverno', 'outono']
    if mes <= 3:
        return estacoes[0]
    elif mes <= 6:
        return estacoes[1]
    elif mes  <= 9:
        return estacoes[2]
    elif mes <= 12:
        return estacoes[3]
    else:
        print("digite um mes.")                
print(estacao_do_tempo(7))