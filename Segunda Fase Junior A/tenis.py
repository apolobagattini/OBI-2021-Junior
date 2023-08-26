def i(): return input()
def ii(): return int(input())
def iis(): return map(int, input().split())
def liis(): return list(map(int, input().split()))
def print_array(a): print(' '.join(map(str, (a+1))))
a=ii()
b=ii()
c=ii()
d=ii()
todos=[a, b, c, d]
ordem=sorted(todos)
dupla1=ordem[0]+ordem[3]
dupla2=ordem[1]+ordem[2]
if dupla1>=dupla2:
    print(dupla1-dupla2)
else:
    print(dupla2-dupla1)