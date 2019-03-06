lst = [int(i) for i in input().split()]
x = int(input()) 
l=len(lst)
z=[]
j=0
if x not in lst:
    print('Отсутствует')
else:
    while j < l:
        if lst[j] == x:
            z+=[j]
        j+=1
    for i in z:
        print(i, end = ' ')


"""  for i in lst:
        while j < l:
            if lst[j] == x:
                z+=[j]
            j+=1
    print(z) """
