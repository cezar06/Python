def ex9(matrix):
    list_of_tuples = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(i):
                if matrix[i][j] <= matrix[k][j]:
                    list_of_tuples.append((i,j))
                    break
    return list_of_tuples


print(ex9([[1, 2, 3, 2, 1, 1],

 [2, 4, 4, 3, 7, 2],

 [5, 5, 2, 5, 6, 4],

 [6, 6, 7, 6, 7, 5]]))
