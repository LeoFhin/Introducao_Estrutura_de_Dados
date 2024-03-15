#Aluno: Leonardo Santos de Lima
#Turma: P2b

#Questão 7 - Escreva um programa que cria uma lista de números inteiros e exibe os números pares da lista.

from random import randint as rd

list_num = []
list_par = []

max_random = rd(1, 10)  # Definindo um limite

# Preenchendo a lista com números aleatórios
for i in range(max_random):
    list_num.append(rd(1, 20))

# Iterando sobre a lista para encontrar os números pares
for i in list_num:
    if i % 2 == 0:
        list_par.append(i)

print(f"Esses são os números pares da lista: {list_par}")