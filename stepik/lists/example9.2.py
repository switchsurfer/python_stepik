a=[int(input())]
while sum(a) != 0:
    a.append(int(input()))
x = (sum([i*i for i in a]))
print(x)