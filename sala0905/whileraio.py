import math
listaarea = []
while True:
    raio = float(input("qual o raio do circulo?"))
    area = float(math.pi*raio**2)
    listaarea.append(area)
    formatado  = [f"{x:.2f}" for x in listaarea]
    print (f"a area do circulo é {formatado}")
    continuar = str(input("quer continuar?"))
    if continuar == "nao":
        break