### Invert every left and right of input binary tree using iterative BFS
###
import collections

def invert_tree(root):
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()

        node.left, node.right = node.right, node.left
        queue.append(node.left)
        queue.append(node.right)

    return root