for i in range (5):
    sexo = str(input("insira seu genero"))
    if (sexo != "f") and (sexo != "m"):
        print ("insira resposta valida")
    elif sexo == "m":
        altura = float(input("insira altura"))
        pesoideal = (72.7*altura) - 58
        print (pesoideal)
    elif sexo == "f":
        altura = float(input("insira altura"))
        pesoideal = (62.1*altura) - 44.7
        print (pesoideal)