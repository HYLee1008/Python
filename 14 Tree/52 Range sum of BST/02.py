### Calculate sum of every node bigger than L, smaller than R when BST is given using DFS pruning
### Optimized version
from datastructure import TreeNode


def range_sum_bst(root, L, R):
    def dfs(node):
        if not node:
            return 0

        if node.val < L:
            return dfs(node.right)
        elif node.val > R:
            return dfs(node.left)
        return node.val + dfs(node.left) + dfs(node.right)

    return dfs(root)
