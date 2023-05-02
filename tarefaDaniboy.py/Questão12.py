import math

#Declaração de Variáveis
num : int 
contNumPrimo : int 
quantNumPrimo : int

num = 0
contNumPrimo = 0
quantNumPrimo = 0 

#Entrada de Dados
for n in range(1, 11):
    num = int(input("Informe um número: "))

#Processamento de Dados
    for m in range(2, int(math.sqrt(num) + 1)):
        if num % m == 0:
            contNumPrimo = contNumPrimo + 1

    if contNumPrimo == 0:
        quantNumPrimo = quantNumPrimo + 1

    contNumPrimo = 0

#Saída de Dados
print(f"A quantidade de números primos são de: {quantNumPrimo}")