#Faça um programa que calcule a média de três números inseridos pelo usuário.

#Aluno = Leonardo santos de lima. P2-B

notas = [] #lista para receber o valor de num

for i in range(3): #loop para o recebimento dos valores
   
    num = float(input('Dígite a nota: ')) 
    notas.append(num) #append adiciona o valor ao fim da lista

media = sum(notas) / len(notas) # sum soma todas os valores da lista, enquanto len determina o numero total de elementos dentro da lista

print(f'A sua média é: {media:.2f}')