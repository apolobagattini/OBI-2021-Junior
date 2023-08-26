saldo=0
for i in range(6):
    resultado=input()
    if resultado=="V":
        saldo+=1
if saldo>=5:
    print("1")
elif saldo<5 and saldo>2:
    print("2")
elif saldo<3 and saldo>0:
    print("3")
else:
    print("-1")