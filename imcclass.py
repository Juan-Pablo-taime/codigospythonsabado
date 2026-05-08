peso = float(input("insira seu peso"))
altura = float (input("insira sua altura"))
imc = peso/(altura**2)
if imc < 18.5:
    print (f"vc esta abaixo do peso {imc}")
elif imc >= 18.5 and imc <= 24.9:
    print (f"vc esta no peso normal {imc}")
elif imc >= 25 and imc <= 29.9:
    print (f"vc esta sobrepeso {imc}")
else:
    print (f"vc esta em obesidade {imc}")