ingressos: float; qntIngressos: int; desp: int; renda: float; lucro: float

import os

ingressos = 5
desp = 200
qntIngressos = 120

os.system("cls")

while ingressos >= 1:
    renda = ingressos * qntIngressos
    lucro = renda - desp
    print(f"|O preço do ingresso é: \t\t    {ingressos:.1f} |")
    print(f"|A quntidade de ingresssos vendidos é: \t    {qntIngressos} |") 
    print(f"|O lucro com essa quanidde de ingressos é: {lucro:.1f}|")
    print("=" *49)
    qntIngressos += 26
    ingressos -= 0.5