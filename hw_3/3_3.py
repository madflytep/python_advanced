class HashMixin:
    def __hash__(self):
        """
        A simple hash function for a matrix that works like this:
         - Sums up all elements of the matrix.
         - Calculates the product of the sum of elements and the number of rows of the matrix.
         This does not guarantee that the hash is unique for all possible matrices,
         but provides different hash values for matrices of different sizes and contents.
        """
        return hash((sum(sum(row) for row in self.matrix), len(self.matrix) * len(self.matrix[0])))

class MatrixOperationsMixin:
    def __add__(self, other):
        # Сложение матриц
        return MatrixWithOperations([[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))])

    def __matmul__(self, other):
        # Матричное умножение
        result = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*other.matrix)] for X_row in self.matrix]
        return MatrixWithOperations(result)

class MatrixWithOperations(MatrixOperationsMixin, HashMixin):
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

def save_matrix(matrix, filename):
    with open(filename, "w") as f:
        f.write(str(matrix))

def find_collision_and_save():
    # Пример генерации матриц для демонстрации коллизии
    A = MatrixWithOperations([[1, 2], [3, 4]])
    B = MatrixWithOperations([[4, 3], [2, 1]])
    C = MatrixWithOperations([[2, 3], [4, 5]])
    D = B  # B и D равны

    # Сохраняем матрицы
    save_matrix(A, "artifacts/3.3/A.txt")
    save_matrix(B, "artifacts/3.3/B.txt")
    save_matrix(C, "artifacts/3.3/C.txt")
    save_matrix(D, "artifacts/3.3/D.txt")

    # Умножение матриц и сохранение результатов
    AB = A @ B
    CD = C @ D
    save_matrix(AB, "artifacts/3.3/AB.txt")
    save_matrix(CD, "artifacts/3.3/CD.txt")

    # Проверка коллизии хэшей и сохранение
    with open("artifacts/3.3/hash.txt", "w") as f:
        f.write(f"Hash of A: {hash(A)}\nHash of C: {hash(C)}\nHash of AB: {hash(AB)}\nHash of CD: {hash(CD)}")

    return "Files saved: A.txt, B.txt, C.txt, D.txt, AB.txt, CD.txt, hash.txt"

# Вызов функции для выполнения задачи
find_collision_and_save()
