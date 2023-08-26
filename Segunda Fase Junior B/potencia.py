def ii(): return int(input())
n=ii()
total=0
for i in range(n):
    numero=ii()
    total+=((numero//10)**(numero%10))
print(total)