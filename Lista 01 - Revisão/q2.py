#Crie um programa que determine se um número inserido pelo usuário é par ou ímpar.

#Aluno = Leonardo santos de lima. P2-B

num = int(input('Digite um número: '))  #variavel para receber o número

if num % 2 == 0:                        #se o resto da divisão for igual a 0 faça:
    print(f'O número {num} é PAR.')
else: #se não:
    print(f'O número {num} é IMPAR.')