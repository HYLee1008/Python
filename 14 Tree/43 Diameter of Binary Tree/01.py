### Calculate the diameter of binary tree using DFS
###
from datastructure import *


class Solution:
    longest = 0
    def diameter_of_binary_tree(self, root):
        def dfs(node):
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left + right + 2)

            return max(left, right) + 1

        dfs(root)
        return self.longest


input = TreeNode(1)
input.left = TreeNode(2)
input.right = TreeNode(3)
input.left.left = TreeNode(4)
input.left.right = TreeNode(5)

sol = Solution()
print(sol.diameter_of_binary_tree(input))