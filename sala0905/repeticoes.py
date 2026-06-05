'''testando teste testador'''
lista = []
while True:
    valor = int(input("insira lista"))
    valor = int(valor**2)
    lista.append (valor)
    continuar = str(input("quer continuar?"))
    if continuar == "nao":
        break
print (lista)
