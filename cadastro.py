idade = int(input("insira sua idade"))
if idade <= 12:
    print ("vc é uma  criança=")
elif idade >= 13 and idade <=17:
    print ("vc é adolescente")
elif idade >= 18 and idade <=59:
    print ("vc é adulto")
else:
    print ("vc é idoso")