def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis(): return list(map(int, input().split()))
def print_array(a): print(' '.join(map(str, (a+1))))
alfabeto = ["a", "b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z']
frase=input()
count=0
for i in alfabeto:
    if i in frase:
        count+=1
if count==23:
    print("S")
else:
    print("N")