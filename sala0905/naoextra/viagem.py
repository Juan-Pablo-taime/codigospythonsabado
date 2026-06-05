viagens = int(input("insira a quantidade de viagens realizadas"))
entregatotal= 0 
i = 1
for i in range (1, (viagens + 1)):
    entrega = int(input(f"digite o numero de entregas da viagem {i}"))
    entregatotal += entrega
mediadeviagem = (entregatotal/viagens)
print(f"a media de entrega por viagem foi de {mediadeviagem}")