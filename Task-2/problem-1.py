matrix1=[]
for i in range (0,5):
        matrix1.append(list(map(int,(input().split()))))
for i in range(0,len(matrix1)):
    for j in range(0,len(matrix1)):
        if matrix1[i][j] == 1 :
            num_of_moves=abs(j-2)
    if 1 in matrix1[i] :
        num_of_moves+=abs(i-2)
print(num_of_moves)