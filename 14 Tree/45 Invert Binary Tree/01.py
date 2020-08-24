### Invert every left and right of input binary tree using pythonic method
###
def invert_tree(root):
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

