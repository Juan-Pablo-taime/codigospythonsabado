total = 0
while True:
    print ("---mercadinho alisalmeupelo---")
    print ("--- 1 arroz R$6.50---")
    print ("--- 2 feijao R$8.00---")
    print ("--- 3 farinha R$5.00---")
    print ("---finalize digitando 0---")
    resp = int(input("insira o numero do produto que desejas"))
    match resp:
        case 1:
            total = total + 6.50
            print ("arroz adicionado ao total das compras")
        case 2:
            total = total + 8.00
            print (" feijão adicionado ao total das compras")
        case 3:
            total = total + 5.00
            print ("farinha adicionada ao total de compras")
        case 0:
            break
print (total)