import numpy as np

class PythonMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrices must have the same dimensions for addition.")
        return PythonMatrix(
            [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        )
    
    def __mul__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrices must have the same dimensions for element-wise multiplication.")
        return PythonMatrix(
            [[self.matrix[i][j] * other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        )
    
    def __matmul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix.")
        result = [[sum(a*b for a, b in zip(row, col)) for col in zip(*other.matrix)] for row in self.matrix]
        return PythonMatrix(result)
    
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])


def generate_matrix(size, seed):
    np.random.seed(seed)
    return [[np.random.randint(0, 10) for _ in range(size)] for _ in range(size)]

# Generate matrices
matrix1 = PythonMatrix(generate_matrix(10, 0))
matrix2 = PythonMatrix(generate_matrix(10, 1))

# Perform operations
addition_result = matrix1 + matrix2
elementwise_multiplication_result = matrix1 * matrix2
matrix_multiplication_result = matrix1 @ matrix2

# Save results to files
with open("artifacts/3.1/matrix+.txt", "w") as f:
    f.write(str(addition_result))

with open("artifacts/3.1/matrix*.txt", "w") as f:
    f.write(str(elementwise_multiplication_result))

with open("artifacts/3.1/matrix@.txt", "w") as f:
    f.write(str(matrix_multiplication_result))
