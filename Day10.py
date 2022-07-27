#Loops
condition = 1
while condition < 9:
   # print(condition)
    condition += 1
    if condition ==8:# ele printa
        break

#The above while loop only prints 0, 1, 2 and 4 (skips 3).



# duas maneiras de se fazer um for
#language = 'Python'
#for letter in language:
    #print(letter)


#for i in range(len(language)):
    #print(language[i])

#Escreva um loop que faça sete chamadas para print()
# , então temos na saída o seguinte triângulo:
# ele printa um e depois printa denovo...

# recebe a quantidade de triângulos e opcionalmente um separador
rows = 5
for i in range(rows +1):#numeros de linhas
    for j in range(i):
        i = '#'
        print(i, end='')  # end = um espaco, uma linha.
    print('')# um embaixo do outro

# printi de um quadrado de #
quadrado = 2
for i in range(quadrado + 4):  # numeros de linhas
    for j in range(i):
        if i:
            i = '#'
            print("##################")
        #print(i)  # end = um espaco, uma linha.
    #print('')


#tabuada de n(0, 10) * n(0,10)
#print n * n = x

for a in range(0, 11):
    total = a * a
    print(f"{a} x {a} = {total}")
    #for a in range(a + b):
        #print(f"{a} * {b} = {total}")
