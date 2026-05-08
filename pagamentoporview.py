vizu= int(input("insira sua quantidade de vizualição"))
if vizu <= 10000:
    print ("SEM MONETIZAÇÃO")
elif vizu >= 10001 and vizu <= 100.000:
    moneti = (vizu * 0.02)
    print (f"sua monetização {moneti}")
elif vizu >= 100.001 and vizu <= 1.000000:
    moneti = (vizu * 0.03)
    if vizu >= 500000:
        moneti = moneti + 500
    print (f"sua monetização {moneti}")
else:
    moneti = (vizu * 0.05)
    if vizu >= 500000:
        moneti = moneti + 500
    print (f"sua monetização {moneti}")
    

