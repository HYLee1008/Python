### Count the number of island
###
def num_is_island(grid):
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return

        grid[i][j] = 0

        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count

input_1 = [list('11110'), list('11010'), list('11000'), list('00000')]
input_2 = [list('11000'), list('11000'), list('00100'), list('00011')]

print(num_is_island(input_1))
print(num_is_island(input_2))

