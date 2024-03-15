#Aluno: Leonardo Santos de Lima
#Turma: P2b

#Questão 10 - Escreva um programa que cria uma lista de números inteiros e remove todos os números repetidos,
#exibindo a lista resultante.

from random import randint as rd

list_1 = []
list_2 = []
lista_final = []

max_random = rd(1, 10)

for i in range(max_random):
    list_1.append(rd(1, 20))

for i in range(max_random):
    list_2.append(rd(1, 20))

# Juntando as duas listas em uma única lista
merged_list = list_1 + list_2

print(f"Lista 1: {list_1}")
print(f"Lista 2: {list_2}")

for num in merged_list:
    if num not in lista_final:
        lista_final.append(num)

print("Lista final sem números repetidos:", lista_final)