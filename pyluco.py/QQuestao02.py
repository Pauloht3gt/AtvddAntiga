from ctypes.wintypes import PINT


pesosaco = float(input("Informe o peso do saco de ração: "))
gramas =float(input("informe a quantidade de racão dada para cada gato: "))


pesofinal = pesosaco - (gramas*2)

print(f"sobrara{pesofinal} kg apos 5 dias")
