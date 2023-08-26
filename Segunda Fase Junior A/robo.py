def iis(): return map(int, input().split())
n, c, s=iis()
comandos=map(int, input().split())
movimento=1
count=0
if movimento==s:
    count+=1
for i in comandos:
    movimento+=i
    if movimento<1:
        movimento=n
    if movimento>n:
        movimento=1
    if movimento==s:
        count+=1
print(count)