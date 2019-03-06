""" genome = input()+' '
s = 0
n=genome[0]
for i in genome:       
    if n!=i:
        print(n + str(s), end = '')
        s=0
        n=i
    s+=1 """

s = input()+' '
g = 0
n=s[0]
for i in s:
    if n!=i:
        print(n+str(g), end= '')
        g=0
        n=i
    g+=1    
