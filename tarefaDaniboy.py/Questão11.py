#Declaração de Variáveis
valorDoCarro : float; precoAVista : float; taxaJuros : float

valorDoCarro = 0.0
precoAVista = 0.0
taxaJuros = 0.03

#Entrada de Dados
valorDoCarro = float(input("Informe o valor do carro: "))

#Processamento e Saída de Dados
precoAVista = valorDoCarro - (precoAVista * 0.20 )
print("QUANTIDADE DE PARCELAS - % JUROS")
print("--------------------------------")
for n in range(6, 66, 6):
    print(f"{n} - {valorDoCarro + valorDoCarro * taxaJuros}") 
    taxaJuros = taxaJuros + 0.03