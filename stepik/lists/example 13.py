n = int(input())
x=[[0 for i in range(n)]for i in range(n)]
row = 0
col = 0
z=1
while z < n*n+1:
        while row < n:
                while col < n:
                        x[row][col]=z
                        col+=1
                        z+=1
                row+=1
                col=0        
        z+=1                
print(x)


