#a,b=(int(i) for i in input().split())
a=int(input())
b=(int(input()))
s=0
c=0
for j in range(a,b+1):
    if j % 3 == 0:
        s+=j
        c+=1
    print(iter(j))
c=(s/c)
print(c)        