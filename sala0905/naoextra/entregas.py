totalentreg = 0
while True: 
    entrega = int(input("quantas entregas vc fez nessa viagem"))
    totalentreg = totalentreg + entrega
    if entrega == 0:
        break
print (totalentreg)

