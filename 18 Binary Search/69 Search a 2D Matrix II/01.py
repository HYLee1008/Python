### Find the target value in the sorted 2D matrix
###
def search_matrix(matrix, target):
    if not matrix:
        return False

    row = 0
    col = len(matrix[0]) - 1

    while row <= len(matrix) - 1 and col >= 0:
        if target == matrix[row][col]:
            return True
        elif target < matrix[row][col]:
            col -= 1
        elif target > matrix[row][col]:
            row += 1
    return False