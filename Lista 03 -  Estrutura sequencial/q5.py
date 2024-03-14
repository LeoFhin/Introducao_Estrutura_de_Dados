#Aluno: Leonardo Santos de Lima
#Turma: P2b

#Escreva um programa que cria uma lista de palavras e exibe a quantidade de palavras que começam
#com a letra 'A'.

lista_nome = ["leonardo", "Akila", "Navori", "Atreus", "Andromeda", "Athenas"]

contador_a = 0

for i in lista_nome: 

    if i[0].upper() == "A": 

        contador_a += 1 

print(f"A lista {lista_nome} possui {contador_a} nomes que começam com 'A'.")