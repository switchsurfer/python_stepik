a = input().lower()

cnt=0

for i in a:
    if i == 'c':
        cnt+=1
    elif i == 'g':
        cnt +=1
print(cnt/len(a)*100)


#print(a.lower().count('c'))




