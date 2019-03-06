a = [int(i) for i in input().split()]
l=len(a)
r=[]
i=0
while i < l:
    if l==1:
        r+=a
        break   
    if i == (l-1):
        r+=[(a[i-1] + a[0])]
    else:
        r+=[(a[i-1]+a[i+1])]
    i+=1
for j in r:
    print(j,end =' ')