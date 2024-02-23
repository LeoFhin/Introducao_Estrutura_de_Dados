#Crie um programa que leia uma lista de números e exiba o maior e o menor valor da lista.

#Aluno = Leonardo santos de lima. P2-B

lista = [] #lista para guardar os valores
entradas = int(input('Dígite o número de entradas: '))

for i in range(entradas): #loop para arrecadar os valores 

    num = int(input('Informe o valor: '))
    lista.append(num) #append adiciona os valores ao final da lista

print(f'o maior valor da lista é: {max(lista)}') #min pega o maior valor da lista
print(f'O menor valor da lista é: {min(lista)}') #min puxa o menor valor da lista