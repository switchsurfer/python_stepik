def modify_list(l):
    cnt=(len(l))
    i = 0
    while cnt != 0:
        if l[i]%2 == 0:
            l[i] = int(l[i]/2)
            i+=1
        else:
            l.remove(l[i])
        cnt-=1    
    return
        

lst = [1,2,3,4,5,6]
print(modify_list(lst))
print(lst)
modify_list(lst)
print(lst)