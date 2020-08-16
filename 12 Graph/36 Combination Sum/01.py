### Find every combination which can make the target value using DFS
###
def combination_sum(candidates, target):
    result = []

    def dfs(csum, index, path):
        if csum < 0:
            return
        elif csum == 0:
            result.append(path)
            return

        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])


    dfs(target, 0, [])
    return result

print(combination_sum([2, 3, 6, 7], 7))
print(combination_sum([2, 3, 5], 8))