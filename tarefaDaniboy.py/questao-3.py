fax1 = 0
fax2 = 0
fax3 = 3
fax4 = 0
fax5 = 0
for n in range(0,8):
    idad = int(input("Digite uma idade: "))
    if idad <= 15:
        idad = fax1
    elif idad <= 30:
        idad = fax2
    elif idad <= 45:
        idad = fax3
    elif idad <= 60:
        idad = fax4
    else:
        idad = fax5
print(f"faixa etária 1 (até 15 anos ): {fax1}") 
print(f"faixa etária 2 (16 a 30 anos ): {fax2}")
print(f"faixa etária 3 (32 a 45 anos ): {fax3}")
print(f"faixa etária 4 (46 a 60 anos ): {fax4}")
print(f"faixa etária 5 (acima de 60 anos ): {fax5}")

print(f"Porcentagem de pessoas com até 15 anos:{fax1/8*100}%")
print(f"Porcentagem de pessoas acima de 60 anos:{fax5/8*100}%")