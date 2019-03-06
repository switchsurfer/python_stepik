n = int(input())
x = [i for i in range(n+1) for j in range(i)]
print(*x[:n])
    