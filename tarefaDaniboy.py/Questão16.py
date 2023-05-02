#Declaração de Variáveis
idade : int 
somaDasIdades : int 
contDasIdades : int 
mediaDasIdades : float 

idade = 1
somaDasIdades = 0
contDasIdades = 0
mediaDasIdades = 0

#Entrada de Dados
while idade != 0:
    idade = int(input("Digite sua idade: "))

#Processamento de Variáveis
    somaDasIdades += idade
    contDasIdades = contDasIdades + 1

mediaDasIdades = somaDasIdades / (contDasIdades - 1)

#Saída de Dados
print(f"A média de idades informadas fora de: {mediaDasIdades}")