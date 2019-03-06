n = int(input())
d={}
for i in range(n):
    n = int(input())
    if n not in d:
        d[n]=f(n)
    print(d[n])

