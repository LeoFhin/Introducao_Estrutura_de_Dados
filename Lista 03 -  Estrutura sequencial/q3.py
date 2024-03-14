#Aluno: Leonardo Santos de Lima
#Turma: P2b

#Questão 3 - Escreva um programa que cria uma lista de números inteiros e exibe a soma de todos os números da
#lista.

from random import randint as rd

max_random = rd(1, 5) #quatidade aleatoria de numero maximo da lista

list_num_int = list(range(1, max_random))

soma_list_num = 0 

for i in list_num_int:
    soma_list_num += i

print(f"A soma dos numeros da lista {list_num_int} é: {soma_list_num}")
