### Calculate sum of every node bigger than L, smaller than R when BST is given using iterative DFS
### Optimized version
from datastructure import TreeNode


def range_sum_bst(root, L, R):
    stack, sum = [root], 0

    while stack:
        node = stack.pop()
        if node:
            if node.val > L:
                stack.append(node.left)
            if node.val < R:
                stack.append(node.right)
            if L <= node.val <= R:
                sum += node.val
    return sum
