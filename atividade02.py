# numeros = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}

numeros = []
for intem in range(20):
    numero = int(input("Digite um número: "))
    numeros.append(numero)
pares = []
impares = []
for numero in numeros:
     if numero % 2 == 0:  
        pares.append(numero)  
     else:
        impares.append(numero)  

print("Números pares:", pares)
print("Números ímpares:", impares)
