### Find the longest univalue path using DFS
###
from datastructure import *

result = 0

def longest_univalue_path(root):
    def dfs(node):
        global result

        if node is None:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        if node.left and node.left.val == node.val:
            left += 1
        else:
            left = 0

        if node.right and node.right.val == node.val:
            right += 1
        else:
            right = 0

        result = max(result, left + right)

        return max(left, right)

    dfs(root)
    return result


input_1 = TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(5, right=TreeNode(5)))
input_2 = TreeNode(1, TreeNode(4, TreeNode(4), TreeNode(4)), TreeNode(5, right=TreeNode(5)))

print(longest_univalue_path(input_1))
print(longest_univalue_path(input_2))