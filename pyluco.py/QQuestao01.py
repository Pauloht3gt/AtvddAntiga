pes: float; jardas: float; mi:float; pol:float

pes = float(input("Digite sua medida: "))

jardas = pes / 3
pol = pes * 12
mil = jardas / 760


print(f"Sua medida em JANDA:{round(jardas,2)}")
print(f"Sua medida em POLEGADAS:{round(pol,2)}")
print(f"Sua medida em MILHAS:{round(mil,2)}")