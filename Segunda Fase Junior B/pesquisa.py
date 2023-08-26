estados=int(input())
vale=[]
for i in range(estados):
    precos=list(input().split())
    alcool=float(precos[1])
    gasolina=float(precos[2])
    if alcool<=(gasolina*0.7):
        vale.append(precos[0])
if len(vale)==0:
    print("*")
else:
    print(f"\n".join(map(str, vale)))