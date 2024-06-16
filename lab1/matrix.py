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
    

if __name__ == "__main__":

    matrix = Matrix([[1, 0 ,2], [-1, 3, 1]], 0)

    matrix_transposed = transpose(matrix)
    print(matrix_transposed)

    matrix2 = Matrix((2, 3), 1)

    matrix3 = matrix + matrix2
    print(matrix3)

    matrix4 = Matrix([[3, 1], [2, 1], [1, 0]])
    matrix5 = matrix2 * matrix4
    print(matrix5)

    



    
    


    
