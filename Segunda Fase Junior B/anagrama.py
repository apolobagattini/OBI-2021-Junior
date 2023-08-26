letras=int(input())
palavra1=list(input())
palavra2=list(input())
count=0
for i in palavra1:
    if i in palavra2:
        count+=1
if count==letras:
    print("S")
else:
    print("N")