#Crie um programa que imprima a sequência de Fibonacci até um valor inserido pelo usuário.

# Aluno: Leonardo santos de lima - P2-B


list_fib = [0, 1] # Cria uma lista

# input para o número limite
numero = int(input("Digite um número limite para a sequência de Fibonacci: "))

while list_fib[-1] + list_fib[-2] <= numero: # Ira ficar repetindo até chegar ou ultrapassar 'numero'
    
    result = list_fib[-1] + list_fib[-2] # Fará a logica da sequencia e armazenar o resultado em 'result'
    list_fib.append(result) # Adiciona o número a lista

# Imprime os resultados
print(f"Resultado da Sequência de Fibonacci até o número {numero}: {list_fib}")