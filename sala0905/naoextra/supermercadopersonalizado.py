produtos = []
valortotal = float(0)
while True:
    produtos.append(input("insira nome do produto"))
    preco = float(input("insira preco do produto"))
    valortotal = valortotal + preco
    continuar = (input("adicionar novo produto?"))
    if continuar == "sim":
        pass
    else:
        break
print(f"o preco das comprars {produtos} e o valor total é de R${valortotal}")