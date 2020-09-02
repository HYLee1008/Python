### Find the target value in the sorted 2D matrix
### Pythonic method
def search_matrix(matrix, target):
    return any(target in row for row in matrix)