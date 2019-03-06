x = []
y = []
a = [i for i in input().split()]

while a[0] != 'end':
    for i in a:
        if i != ' ':
            x += [int(i)]
    y += [x]
    x = []                
    a = [i for i in input().split()]


row = len(y)
col = len(y[0])

i = 0 

x = [[int(0) for j in range(col)]for i in range(row)]
 
for i in range(row):    
    for j in range(col):
        z = y[i-1][j] + y[ i-row +1][j] + y[i][j-1] + y[i][j-col+1]  
        x[i][j] = z

i=0
j = 0
while i < row:
    while j < col:
        print(x[i][j], end = ' ')
        j+=1
    print()
    i+=1
    j=0









        
                  





