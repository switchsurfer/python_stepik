n, m, k = (int(i) for i in input().split()) #вводим количество строк, столбцов и мин соответственно

a = [[0 for j in range(m)] for i in range(n)]  #создаём двумерный массив и заполняем его нулями

for i in range(k):
    row, col = (int(i) - 1 for i in input().split()) #ЗДЕСЬ ВВОДИМ КООРДИНАТЫ int(i) - 1 т.к. в программе индексация начинается с 0, а номера позиций выводятся с единицы    
    a[row][col] = -1 #когда получили координаты, записываем в эту "ячейку" -1 (мина)

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            for di in range(-1,2):      #до 2, т.к. '2' не включается
                for dj in range(-1,2): 
                    ai = i + di
                    aj = j + dj
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
                        a[i][j] += 1

for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print('*', end='')
        elif a[i][j] == 0:
            print('.', end='')
        else:
            print(a[i][j], end='')
    print()


