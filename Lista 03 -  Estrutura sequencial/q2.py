#Aluno: Leonardo Santos de Lima
#Turma: P2b

#Questão 2 - Escreva um programa que cria uma lista de nomes e exibe o número total de nomes na lista.

lista_nomes = ["Leonardo", "Amanda", "Nathielly", "Romeo"]

cont_lista = 0

for i in lista_nomes:
    cont_lista = cont_lista + 1

print(f"A lista possui {cont_lista} nomes.")