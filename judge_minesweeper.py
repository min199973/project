col,row = map(int,input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))

for i in range(col):
    for j in range(row):
        count = 0
        if matrix[i][j] == ".":
            for y in range(i - 1,i + 2):
                for x in range(j - 1,j + 2):
                    if not (y < 0 or x < 0 or y>=row or x>=col):
                        if matrix[y][x] =="*":
                            count+=1
            matrix[i][j] = count
            print(matrix[i][j],end='')
        else:
            print(matrix[i][j],end='')
    print()
                    