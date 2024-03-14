#Aluno: Leonardo Santos de Lima
#Turma: P2b

#Escreva um programa que cria uma lista de números inteiros e exibe a média dos números da lista.

from random import randint as rd

max_random = rd(1, 5) #cria o range maximo da lista

list_num_int = list(range(1, max_random))

soma_list_num = 0 
cont = 0

for i in list_num_int:
    soma_list_num += i
    cont += 1

media = soma_list_num / cont

print(f"A média da lista é: {media}")