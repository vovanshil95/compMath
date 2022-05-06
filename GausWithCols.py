import numpy as np


np.set_printoptions(suppress=True, precision = 4)

class Info:

    def __init__(self, determinant, triangleMatrix, roots, nevs):
        self.determinant = determinant
        self.triangleMatrix = triangleMatrix
        self.roots= roots
        self.nevs = nevs

    determinant: float
    triangleMatrix: np.ndarray
    roots: np.ndarray
    nevs: np.ndarray

def gausWithCols(matrix, vector):

    def getRoots(matrix, vector):
        size = matrix.shape[0]
        roots = np.zeros(size)
        for i in range(size - 1, -1, -1):
            roots[i] = (vector[i] - sum(roots * matrix[i])) / matrix[i][i]
        return roots

    determinant = np.linalg.det(matrix)
    size = matrix.shape[0]
    firstMatrix = matrix.copy()
    firstVector = vector.copy()

    if determinant == 0:
        raise Exception("determinant must be not zero")
    elif matrix.shape[0] != matrix.shape[1]:
        raise Exception("matrix must be square")
    elif matrix.shape[0] != vector.shape[0]:
        raise Exception("dimension of the matrix must be equal to the vector")

    for i in range(size):
        maxIndex, maxx = max(enumerate(matrix.transpose()[i]), key=lambda t: abs(t[1]) if t[0] >= i else 0)
        matrix[i], matrix[maxIndex] = np.copy(matrix[maxIndex]), np.copy(matrix[i])
        vector[i], vector[maxIndex] = vector[maxIndex], vector[i]
        odds = matrix.transpose()[i]/maxx
        for j in range(i+1, len(odds)):
            matrix[j] = matrix[j] - odds[j] * matrix[i]
            vector[j] = vector[j] - odds[j] * vector[i]

    roots = getRoots(matrix, vector)
    errors = np.vectorize(abs)(np.dot(firstMatrix, roots) - firstVector)

    return Info(determinant, matrix, roots, errors)