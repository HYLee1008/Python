### Calculate sum of every node bigger than L, smaller than R when BST is given using recursive DFS
### Brute force method. Not recomendable.
from datastructure import TreeNode


def range_sum_bst(root, L, R):
    if not root:
        return 0

    return (root.val if L <= root.val <= R else 0) + range_sum_bst(root.left, L, R) + range_sum_bst(root.right, L, R)
