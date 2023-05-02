#Declaração de Variáveis
idd : int
peso : float 

mediaDePesos1a10 : float 
mediaDePesos11a20 : float
mediaDePesos21a30  : float
mediaDePesos31Mais : float 

somaDePesos1a10 : float 
somaDePesos11a20 : float 
somaDePesos21a30 : float 
somaDePesos31Mais : float 

quantDePesos1a10 : float
quantDePesos11a20 : float 
quantDePesos21a30 : float 
quantDePesos31Mais : float 

mediaDePesos1a10 = 0
mediaDePesos11a20 = 0
mediaDePesos21a30 = 0
mediaDePesos31Mais = 0

somaDePesos1a10 = 0
somaDePesos11a20 = 0
somaDePesos21a30 = 0
somaDePesos31Mais = 0

quantDePesos1a10 = 0
quantDePesos11a20 = 0
quantDePesos21a30 = 0
quantDePesos31Mais = 0

#Entrada de Dados
for n in range(1 , 16):
    idd = int(input("Informe a sua idade: "))
    peso = float(input("Informe o seu peso: "))

#Processamento e Saída de Dados
    if idd >= 1 and idd <= 10:
        somaDePesos1a10 += peso
        quantDePesos1a10 = quantDePesos1a10 + 1

    if idd >= 11 and idd <= 20:
        somaDePesos11a20 += peso
        quantDePesos11a20 = quantDePesos11a20 + 1

    if idd >= 21 and idd <= 30:
        somaDePesos21a30 += peso
        quantDePesos21a30 = quantDePesos21a30 + 1

    if idd >= 31:
        somaDePesos31Mais += peso
        quantDePesos31Mais = quantDePesos31Mais + 1

if quantDePesos1a10 > 0:
    mediaDePesos1a10 = somaDePesos1a10 / quantDePesos1a10
    print(f"A média de 1 a 10 anos é de: {mediaDePesos1a10}")

else:
    print("Não foram informados pessoas de 1 a 10 anos.")

if quantDePesos11a20 > 0:
    mediaDePesos11a20 = somaDePesos11a20 / quantDePesos11a20
    print(f"A média de 11 a 20 anos é de: {mediaDePesos11a20}")

else:
    print("Não foram informados pessoas de 11 a 20 anos.")

if quantDePesos21a30 > 0:
    mediaDePesos21a30 = somaDePesos21a30 / quantDePesos21a30
    print(f"A média de 21 a 30 anos é de: {mediaDePesos21a30}")

else:
    print("Não foram informados pessoas de 21 a 30 anos.")

if quantDePesos31Mais > 0:
    mediaDePesos31Mais = somaDePesos31Mais / quantDePesos31Mais
    print(f"A média acima de 31 anos é de: {mediaDePesos31Mais}")

else:
    print("Não foram informados pessoas acima de 30 anos.")