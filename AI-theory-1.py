#The Frobenius Norm of a matrix is defined as the square root of
# the sum of the squares of the elements of the matrix.
from math import sqrt

row = 2
col = 2

def frobeniusNorm(mat):
    sumSq = 0
    for i in range(row):
        for j in range(col):
            sumSq += pow(mat[i][j], 2)


    res = sqrt(sumSq)
    return round(res, 5)

m = [[1, 4], [0, (-2)]]    #2x2 matrix

print(frobeniusNorm(m))