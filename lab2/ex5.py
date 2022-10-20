def zero_under_main_diagonal(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j] = 0
    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(zero_under_main_diagonal(matrix))