import numpy as np
from GausWithCols import gausWithCols
from utils import makeZeroes



# matrix = np.array(list(map(lambda el: np.vectorize(int)(el.split(" ")), input("введите матрицу в формате 1 2; 3 4\n").split("; "))), 'double')
# vector = np.array(np.vectorize(int)(input("введите вектор в формате 1 2 3 4\n").split(" ")), 'double')

f = open("input.txt", "r")
inputs = f.read().split("\n\n")
f.close()
for input in inputs:
    matrix = np.array(list(map(lambda el: np.vectorize(int)(el.split(" ")), input.split("\n")[0].split("; "))), 'double')
    vector = np.array(np.vectorize(int)(input.split("\n")[1].split(" ")), 'double')

    info = gausWithCols(matrix, vector)

    print("Matrix:\n", info.triangleMatrix)
    print("roots:\n", makeZeroes(info.roots))
    print("errors:\n", makeZeroes(info.nevs))

    print("\n")