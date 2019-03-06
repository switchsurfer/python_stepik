def update_dict(s, d):
    s = sorted(s)
    cnt = 1
    i=0
    while i+1 < len(s):  
        if s[i] == s[i+1]:
            cnt+=1
            i+=1
            d[s[i]]=cnt
        else:
            d[s[i]]=cnt
            cnt=1
            i+=1
    d[s[i]]=cnt
    return


s = input().lower().split()

            
d = dict()

update_dict(s, d)

for key,value in d.items():
    print(key,value)