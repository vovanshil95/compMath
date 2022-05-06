import numpy as np

def makeZero(a):
    if abs(a-0) < 0.00001:
        return 0
    else:
        return a
makeZeroes = np.vectorize(makeZero)
