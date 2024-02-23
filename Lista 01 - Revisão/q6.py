#Escreva um programa que peça um número inteiro positivo ao usuário e calcule o fatorial desse
#número.

#Aluno = Leonardo santos de lima. P2-B

fatorial = 1

# input de um numero inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

if numero == 0 or numero == 1: # Se o numero for 0 ou 1, faça

    fatorial = 1 # Define o fatorial como 1

else: # Senão

    # Cria um loop com for onde irá calcular o fatorial e armazenar na variavel 'fatorial'
    for i in range(1, numero + 1):

        fatorial *= i

# Imprime o resultado
print(f'O fatorial de {numero} é: {fatorial}')