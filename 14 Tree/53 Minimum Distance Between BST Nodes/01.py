### Find minimum distance between BST nodes using recursive in-order
###
from datastructure import TreeNode
import sys


class Solution:
    prev = -sys.maxsize
    result = sys.maxsize

    def min_diff_in_bst(self, root):
        if root.left:
            self.min_diff_in_bst(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.min_diff_in_bst(root.right)

        return self.result
