from typing import List, Tuple

class Matrix:
    def __init__(self, m, val = 0):
        if isinstance(m, Tuple):
            rows, cols = m
            self.matrix = [[val for _ in range(cols)] for _ in range(rows)]
        else:
            self.matrix = m
    
    def size(self):
        rows, cols = len(self.matrix), len(self.matrix[0])
        return (rows, cols)

    def __add__(self, A):
        if self.size() != A.size():
            return 'Wrong size!'
        else:
            ans = [[i+j for i,j in zip(self.matrix, A)] for self.matrix, A in zip(self.matrix, A)]

            add_result = Matrix(ans)
        return add_result

    def __mul__(self, A):
        if self.size()[0] != A.size()[1] and self.size()[1] != A.size()[0]:
            return 'Wrong size!'
        else:
            rows = self.size()[0]
            cols = A.size()[1]
            ans = [[0 for _ in range(cols)] for _ in range(rows)]

            for i in range(rows):
                for j in range(cols):
                    for k in range(A.size()[0]):
                        ans[i][j] += self.matrix[i][k] * A[k][j]
            
            multiply_result = Matrix(ans)
            
        return multiply_result

    def __getitem__(self, item):
        return self.matrix[item]
    
    def __setitem__(self, key, value):
        self.matrix[key] = value

    def __str__(self):
        rows, cols = self.size()
        result = ""

        for i in range(rows):
            result += "| "
            for j in range(cols):
                result += str(self.matrix[i][j]) + " "
            result += "|\n"

        return result

def transpose(A):
    matrix_transposed = list(zip(*A))
    result = Matrix(matrix_transposed)

    return result
    
def chio_determinant(matrix, multipler = 1):
    if matrix.size() == (2, 2):
        return multipler * two_dim_matrix_determinant(matrix)
    
    if matrix[0][0] == 0:
        for i in range(matrix.size()[0] + 1):
            if matrix[i][0] != 0:
                matrix[0], matrix[i] = matrix[i], matrix[0]
                multipler *= -1
                break
    
    new_mutipler = multipler * (1 / (matrix[0][0] ** (matrix.size()[0] - 2)))

    truncated_matrix = []
    for i in range(matrix.size()[0] - 1):
        new_row = []
        for j in range(matrix.size()[1] - 1):
            new_row.append(two_dim_matrix_determinant(Matrix([[matrix[0][0], matrix[0][j + 1]], [matrix[i + 1][0], matrix[i + 1][j + 1]]])))

        truncated_matrix.append(new_row)

    return chio_determinant(Matrix(truncated_matrix), new_mutipler)

def two_dim_matrix_determinant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]


if __name__ == "__main__":
    A = Matrix([[5 , 1 , 1 , 2 , 3],
                [4 , 2 , 1 , 7 , 3],
                [2 , 1 , 2 , 4 , 7],
                [9 , 1 , 0 , 7 , 0],
                [1 , 4 , 7 , 2 , 2]])

    B = Matrix([[0 , 1 , 1 , 2 , 3],
                [4 , 2 , 1 , 7 , 3],
                [2 , 1 , 2 , 4 , 7],
                [9 , 1 , 0 , 7 , 0],
                [1 , 4 , 7 , 2 , 2]])
    
    print(chio_determinant(A))
    print(chio_determinant(B))    



    
    


    
