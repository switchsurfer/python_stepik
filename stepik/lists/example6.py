a = [int(i) for i in input().split()]
a = sorted(a)
l = len(a)
cnt = 1
for i in range(l-1):
    if a[i] == a[-1]:
        print(a[i])
        break 
    elif a[i] == a[i+1]:
        cnt+=1
    else: 
        if cnt>1:
            print(a[i],end=' ')
            cnt=1
    i+=1
        





 
