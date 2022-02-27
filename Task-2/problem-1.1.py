matrix1=[]
Vertical_move=0
horizontal_move=0
for i in range (0,5):
        matrix1.append(list(map(int,(input().split()))))
for i in range(0,len(matrix1)):
    for j in range(0,len(matrix1)):
        if 1 in matrix1[i]:
            Vertical_move=abs(i-2)
            if matrix1[i][j] == 1 :
                horizontal_move=abs(j-2)
                break
        else:
            break
print(Vertical_move+horizontal_move)