#Escreva um programa que solicite um número ao usuário e imprima todos os números pares de 0 até
#esse número.

numeros = [] #lista para guardar os valores

num = int(input('Dígite um número: ')) #input para receber o valor

for i in range(num + 1): # 'i' assume a funçao de passar por todos o numeros de 0 ao valor que o usuario digitou
    
    if i % 2 == 0: # se 'i' tirer resto 0 (par) adicione o numero a lista. 
        numeros.append(i)
       
print(f'Os numeros pares são: {numeros}')    