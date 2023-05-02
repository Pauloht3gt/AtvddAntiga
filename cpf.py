from random import randint
import os 

#Créditos:
#https://youtu.be/bXX_rQOldeM-Luis Fernando Santos Cardeal


#|Desenvolvendo o gerador de cpf|
def cpfGenerator():
    os.system("cls")

    while True:
        #|Gera os 9 primeiros dígitos do cpf aleatoriamente|
        cpf = [randint(0, 9) for x in range(9)]
        
        #|Verifica se o CPF não é repetido|
        if cpf != cpf[::-1]:
            break
    
    #|Calcula os dígitos verificadores|
    for x in [10, 11]:
        verificator = sum([cpf[x - y] * y for y in range(x, 1, -1)]) * 10 % 11 % 10
        cpf.append(verificator)
        
    #|Converte a o cpf para o modo padrão 123-456-789-xy|
    cpfStr = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpfStr

cpf = cpfGenerator()
print(f"CPF: {cpf}")


repeat = input("\nDo you approve the generated CPF? \n Y-I APPROVE \n N-I DON'T APPROVE \n YOU ANSOWER: ").upper()
if repeat == "Y" or repeat == "YES":
    os.system("cls")
    print(f" excellent!\n Your CPF: {cpf}")

elif repeat == "N" or repeat == "NO":
    os.system("cls")
    repeatCPF = input("Do you want to generate another cpf? \n Y-YES \n N-NO \n YOU ANSOWER: ").upper()

    if repeatCPF == "Y" or repeatCPF == "YES":
        cpf = cpfGenerator()
        print(f"Your New CPF: {cpf}")
        repeat = input("\nDo you approve the generated CPF? \n Y-I APPROVE \n N-I DON'T APPROVE \n YOU ANSOWER: ").upper()
        if repeat == "Y" or "YES":
            os.system("cls")
            print(f" excellent!\n Your CPF: {cpf}")
        elif repeat == "N" or repeat == "NO":
            os.system("cls")
            repeat = input("Do you want to generate another cpf? \n Y-YES \n N-NO \n YOU ANSOWER: ").upper()


    elif repeatCPF == "N" or repeat == "NO":
        os.system("cls")
        cpf = cpfGenerator()
        print(f"CPF: {cpf}")
        print("Sorry for not being enough for you :c")


    else:
        print("The selected option does not exist!")
else:
    print("The selected option does not exist!")