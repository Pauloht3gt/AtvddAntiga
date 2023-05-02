import os
cv = 0
cp = 0
os.system("cls")
c = ""
for n in range(1,4):
    print(f"Dados da {n}ª venda")
    while c != "V" and c!= "P":
        c = input("Digite o código da compra (V - à vista ou P - a prazo): ") .upper()
        if c == "V":
            compra = float(input("Digite o valor da compra: R$ "))
            cv += compra
        elif c == "P":
            compra = float(input("Digite o valor da compra: R$ "))
            cp += compra
        os.system("cls")
    c= ""

print(f"O valor total à vista: R$ {cv:.2f}")
print(f"O valor total a prazo: R$ {cp:.2f}")
print(f"O valor total das compras: R$ {cp +cv:.2f}")
print(f"O valor das compras a prazo juntas: R$ {cp /3:.2f}")