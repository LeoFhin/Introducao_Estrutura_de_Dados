#Faça um programa que determine se um número é primo ou não.

#Aluno = Leonardo santos de lima. P2-B

# input de um numero positivo
numero = int(input("Digite um número inteiro positivo para descobrir se ele é Primo ou não: "))

if numero > 1: # Se 'numero' for maior que 1, então:

    for i in range(2, numero): # Verifica se o número é primo

        if numero % i == 0: # Se o 'numero' for dividido por 'i' e o resto for igual a zero, então:

            print(f"O número {numero} não é primo") # Imprime que não é primo
            break # Encerra o programa

    else: # Senão:

        print(f"O número {numero} é primo") # Imprime que é primo


