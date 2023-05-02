import os

#Declaração de Variáveis
idd : int
op : int 
regular : int 
bom : int 
otimo : int 
mediaDeIdadeOtimo : float 
somaDeIdadeOtimo : float
perBom : float 

otimo = 0 
bom = 0
idd = 0
op = 0
mediaDeIdadeOtimo = 0
somaDeIdadeOtimo = 0
regular = 0

#Entrada de Dados
for n in range(1, 16):
    idd = int(input("Digite sua idade: "))
    op = int(input("\n3 - Ótimo\n2 - Bom\n1 - Regular\nDigite sua opinião: "))

    os.system("cls")
    somaDeIdadeOtimo += idd

#Processamento de Dados
    if op == 3:
        otimo = otimo + 1
        somaDeIdadeOtimo += idade 

    if op == 1:
        regular = regular + 1

    if op == 2:
        bom += 1
        
mediaDeIdadeOtimo = somaDeIdadeOtimo / otimo
perBom = bom / 15 * 100

#Saída de Dados
print(f"A média das idades que respoderam ótimo foi de {mediaDeIdadeOtimo}")
print(f"A quantidade de pessoas que respoderam foi de {regular}")
print(f"A porcentagem de pessoas que respoderam bom foi de {perBom}")