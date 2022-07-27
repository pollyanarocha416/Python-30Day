def gerar_nome():
    nome = 'polly'
    sobrenome = 'rocha'
    spaco = ' '
    nome_completo = nome + spaco + sobrenome
    print("gerando nome..........")
    print(nome_completo)

gerar_nome()


def generate_full_name():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
#print(generate_full_name())


def greetings(name):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings('Pollyana'))



def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))


def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))


#Retornando um booleano: Exemplo:
def is_even(n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break
    return False
print(is_even(10))  # True
print(is_even(7))  # False

#uma lista de numeros pares
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

#ele retorna o petter e a Asabeneh
def greetings(name='Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))


def sum_all_nums(*nums):#quando nao sabe qts argumentos passar
    total = 0
    for num in nums:
        total += num     # same as total = total + num
    return total
print(sum_all_nums(2, 3, 5))  # 10

#Número padrão e arbitrário de parâmetros em funções
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))



#You can pass functions around as parameters
def square_number(n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3))  # 27
