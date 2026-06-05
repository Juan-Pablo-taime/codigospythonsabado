while True:
    peso = float(input("insira seu peso"))
    altura = float (input("insira sua altura"))
    imc = peso/(altura**2)
    print (imc)
    continuar = str(input("quer continuar"))
    if continuar == "nao":
        break