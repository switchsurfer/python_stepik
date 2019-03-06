def min(*a):
    m=a[0]
    for x in a:
        if m > x:
            m = x
    print(a)
    return m

x = min(5)
print(x)

x = min(5,3)
print(x)

x = min(5,3,6,10)
print(x)

x = min([5,3,6,10])
print(x)