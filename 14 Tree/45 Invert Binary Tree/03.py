### Invert every left and right of input binary tree using iterative DFS
###
def invert_tree(root):
    stack = [root]

    while stack:
        node = stack.pop()

        node.left, node.right = node.right, node.left
        stack.append(node.left)
        stack.append(node.right)

    return root