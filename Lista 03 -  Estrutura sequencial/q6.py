#Aluno: Leonardo Santos de Lima
#Turma: P2b

#Questão 6  - Escreva um programa que cria uma lista de strings e exibe a mais longa palavra da lista.

list_palavras = ["Python", "Java", "JavaScript", "Nodejs"]

maior_palvra = max(list_palavras, key = len)

print(f"A palavra mais loga é: {maior_palvra}")