import numpy as np

class ArithmeticMixin:
    def __add__(self, other):
        return type(self)(self.matrix + other.matrix)
    
    def __sub__(self, other):
        return type(self)(self.matrix - other.matrix)
    
    def __mul__(self, other):
        return type(self)(self.matrix * other.matrix)
    
    def __matmul__(self, other):
        return type(self)(self.matrix @ other.matrix)
    
    def __truediv__(self, other):
        return type(self)(self.matrix / other.matrix)

class IOOperationsMixin:
    def to_file(self, filename):
        with open(filename, "w") as f:
            f.write(str(self))
    
    def from_file(cls, filename):
        with open(filename, "r") as f:
            matrix = np.loadtxt(f)
        return cls(matrix)

class DisplayMixin:
    def __str__(self):
        return np.array_str(self.matrix)

class AccessorMixin:
    @property
    def matrix(self):
        return self._matrix
    
    @matrix.setter
    def matrix(self, value):
        self._matrix = np.array(value)

class EnhancedMatrix(ArithmeticMixin, IOOperationsMixin, DisplayMixin, AccessorMixin):
    def __init__(self, matrix):
        self.matrix = matrix

# Generating matrices with numpy for demonstration, assuming numpy is allowed for this part
np.random.seed(0)
matrix_data1 = np.random.randint(0, 10, (10, 10))
matrix_data2 = np.random.randint(0, 10, (10, 10))

matrix1 = EnhancedMatrix(matrix_data1)
matrix2 = EnhancedMatrix(matrix_data2)

# Performing operations
addition_result = matrix1 + matrix2
elementwise_multiplication_result = matrix1 * matrix2
matrix_multiplication_result = matrix1 @ matrix2

# Saving results to files
addition_result.to_file("artifacts/3.2/matrix+.txt")
elementwise_multiplication_result.to_file("artifacts/3.2/matrix*.txt")
matrix_multiplication_result.to_file("artifacts/3.2/matrix@.txt")


