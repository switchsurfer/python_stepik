n = int(input())
j=0
i=0
x=[]
for i in range(n+1):
    while j < i:
        x+=[i]
        j+=1
    j=0
    i+=1
i=0
while i < n :
    print(x[i],end=' ')
    i+=1






