# 7) Write a function to add elements of two input matrices.

def init_sum_matrix(matrix, n):
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        matrix.append(row)
    return matrix


def input_matrix(matrix, n):
    for i in range(n):
        row = []
        for j in range(n):
            row.append(int(input()))
        matrix.append(row)
    return matrix


def sum_of_matrices(matrix1, matrix2, sum_matrix):
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            sum_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

    return sum_matrix


in_matrix1 = []
in_matrix2 = []
sum_matrix = []

num = int(input('Enter N for NXN Matrix: '))
sum_matrix = init_sum_matrix(sum_matrix, num)
print('Enter values for first matrix:')
in_matrix1 = input_matrix(in_matrix1, num)
print('Enter values for second matrix:')
in_matrix2 = input_matrix(in_matrix2, num)
print(f'First Matrix: {in_matrix1}')
print(f'Second Matrix: {in_matrix2}')
sum_matrix = sum_of_matrices(in_matrix1, in_matrix2, sum_matrix)
print(f'Sum of the matrices: {sum_matrix}')
