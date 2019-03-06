s = input()
cnt =0
j=0
i=0
l=len(s)
x=i+1
b=str()
a=str()
while j<l:
    if x+1 > l:
        a=s[i]+str(cnt+1)
        b+=a
        break
    else:
        if s[i] != s[x]:
            cnt+=1
            a=s[i]+str(cnt)
            b+=a
            a=str()
            cnt=0
            i+=1
            x+=1
        elif s[i] == s[x]:
            cnt+=1
            a=s[i]+str(cnt+1)
            x+=1
            i+=1        
    j+=1
print(b)   