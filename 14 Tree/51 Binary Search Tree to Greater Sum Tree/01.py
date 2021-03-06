### Binary search tree to greater sum tree using in-order.
###
from datastructure import TreeNode


class Solution:
    val = 0
    def bst_to_gst(self, root):
        if root:
            self.bst_to_gst(root.right)
            self.val += root.val
            root.val = self.val
            self.bst_to_gst(root.left)
        return root
