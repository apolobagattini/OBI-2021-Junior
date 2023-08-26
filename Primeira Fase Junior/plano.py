def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis(): return list(map(int, input().split()))
def print_array(a): print(' '.join(map(str, (a+1))))
x=ii()
meses=ii()
geral=[]
total=x*meses
for i in range(meses):
    usado=ii()
    geral.append(usado)
for i in geral:
    total-=i
print(total+x)
