lote = int(input("insira a quantidade de lotes que chegaram"))
itenstotal = 0 
i = 1
for i in range (1, (lote + 1)):
    itens = int(input(f"insira a quantidade de itens do lote {i}"))
    itenstotal += itens
print (f"a quantidade total de itens foi de {itenstotal}")
