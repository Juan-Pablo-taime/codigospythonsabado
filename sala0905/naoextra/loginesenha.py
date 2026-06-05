cred = False
while cred == False:
    login = (input("insiralogin"))
    senha = (input("insira senha"))
    if senha != ("1234") and login != ("admin"):
        print ("credencial invalida")
    else:
        print ("bem vindo")
        cred = True