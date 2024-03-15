#Aluno: Leonardo Santos de Lima
#Turma: P2b

#Escreva um programa que cria duas listas de números inteiros e exibe os números que estão presentes
#em ambas as listas.

from random import randint as rd

list_1 = []
list_2 = []
lista_igual = []

max_random = rd(1, 10)

for i in range(max_random):
    list_1.append(rd(1, 20))

for i in range(max_random):
    list_2.append(rd(1, 20))

print(f"Lista 01: {list_1}")
print(f"Lista 02: {list_2}")

for num in list_1:
    if num in list_2 and num not in lista_igual:
        lista_igual.append(num)

print("Números presentes em ambas as listas:", lista_igual)