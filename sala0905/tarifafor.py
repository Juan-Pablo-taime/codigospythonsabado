for i in range (4):
    premium = str(input("sua conta é premium?"))
    if premium == "não":
        saldo = float(input("insira seu saldo"))
        if saldo < 1000:
            print ("sua tarifa é de R$25")
        elif saldo >= 1000 and saldo <= 5000:
            print ("sua tarifa é de R$15")
        else:
            print ("vc esta isento de tarifa")
    else:
        saldo = float(input("insira seu saldo"))
        if saldo < 5000:
            print ("vc tem tarifa de 20 a pagar")
        else:
            print ("não há tarifas a pagar")