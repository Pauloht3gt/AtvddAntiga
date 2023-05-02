#Declaração de Variáveis
sx : str
resp : str 
totalDeSim : int 
totalDeNao : int 
mulheresSim : int
homensNao : int 
homensSim : int 
totalHomens : int 
percHomens : float 
  
sexo = ""
resp = ""
totalDeNao = 0
totalDeSim = 0
mulheresSim = 0
homensNao = 0
homensSim = 0
percHomens = 0
totalHomens = 0

#Entrada de Dados
for n in range(1, 11):
    sx = input("Informe seu sexo |M - Masculino / F - Feminino|: ")
    resp = input("Informe sua resposta |S - Sim / N - Não|: ")

#Processamento de Dados
    if resp == "S":
        totalDeSim = totalDeSim + 1
        if sx == "F":
            mulheresSim = mulheresSim + 1
        else:
            homensSim = homensSim + 1

    if resp == "N":
        totalDeNao = totalDeNao + 1
        if sx == "M":
            homensNao = homensNao + 1

totalHomens = homensNao + homensSim
percHomens = homensNao / totalHomens * 100

#Saída de Dados
print(f"O total de pessoas que dissseram SIM foram de: {totalDeSim}")
print(f"O total de pessoas que dissseram NÃO foram de: {totalDeNao}")
print(f"O total de mulheres que dissseram SIM foram de: {mulheresSim}")
print(f"O percentual de homens que dissseram NÃO foram de: {percHomens}")