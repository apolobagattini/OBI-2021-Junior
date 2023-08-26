n=int(input())
mao1=[]
mao2=[]
if n==0:
    print("*")
    print("*")
elif n<6:
    for i in range(n):
        mao1.append("I")
    print(''.join(mao1))
    print("*")
else:
    for i in range(n-5):
        mao2.append("I")
    print("IIIII")
    print(''.join(mao2))