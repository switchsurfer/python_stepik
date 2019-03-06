n = int(input())
o=[[0 for i in range(n)]for i in range(n)]

square = n*n

x = 0
y = 0

lo = 0

z=1

if n == 0:
    print(0)
else:
    
    while z < square:
    
        
            while x < n-1:        
                o[y][x]=z
                z+=1
                x+=1
            
            
            while y < n-1:       
                o[y][x]=z
                z+=1
                y+=1
            

            while x > lo:
                o[y][x]=z
                z+=1
                x-=1
            

            while y > lo:
                o[y][x]=z
                y-=1
                z+=1

            x+=1
            y+=1
            n-=1
            lo+=1

    if square%2 != 0:
        o[x][y]=z

                

    for i in range(len(o)):
        for j in range(len(o)):
            print(o[i][j], end=' ')
        print()