areaquad = [ ]
area2list = [ ]
for i in range (3):
    base = float(input("insira a base do quadrado"))
    altura = float(input("insira a altura do quadrado"))
    area = base*altura
    area2 = area*2
    areaquad.append(area)
    area2list.append (area2)
    print(f"a area desse quadrado é {areaquad} e o dobro dela é {area2list} ")