#Faça um programa que leia uma lista de números e retorne a média dos números pares.

#Aluno = Leonardo santos de lima. P2-B

numeros = []
entradas = int(input('Dígite o número de entradas: '))

for i in range(entradas):
    
    #input dos numeros em loop
    num = int(input('Dígite o número: '))
    
    # se 'i' tirer resto 0 (par) adicione o numero a lista. 
    if i % 2 == 0: 
        numeros.append(i)

#sum soma todos os numeros da lista / len determina o total de elentos dentro da lista
media = sum(numeros) / len(numeros)

print(f'A média dos números é: {media}')