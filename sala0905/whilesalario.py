listasal = []
while True:
    ganhohora = float(input("quanto vc ganha por hora?"))
    horatrab = int(input ("quantas horas vc trabalhou?"))
    salario = ganhohora*horatrab
    print(f"voce ganhou {salario} este mes")
    listasal.append (salario)
    continuar = str(input("quer continuar?"))
    if continuar == "nao":
        break
print (listasal)