total = 0
while True:
    compras = int(input("insira preço do produto"))
    total = total + compras
    if compras == 0:
        break
print (total)    