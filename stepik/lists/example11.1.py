l = [int(i) for i in input().split()]
x = int(input())
if x not in l: print('Отсутствует')
for i in range(len(l)):
    if l[i] == x : print(i, end=' ')