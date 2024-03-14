#Aluno: Leonardo Santos de Lima
#Turma: P2b

#Questão 1 - Escreva um programa que cria uma lista de números inteiros e exibe o maior número da lista.

# Função para criar uma lista de números inteiros
def criar_lista(numeros):
    return numeros

# Função para encontrar o maior número na lista
def encontrar_maior(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior

# Números para criar a lista
numeros = [8, 10, 7, 27, 5]

# Criar a lista
lista_numeros = criar_lista(numeros)

# Exibir a lista
print("Lista de números:", lista_numeros)

# Encontrar o maior número na lista
maior_numero = encontrar_maior(lista_numeros)

# Exibir o maior número
print("O maior número na lista é:", maior_numero)
