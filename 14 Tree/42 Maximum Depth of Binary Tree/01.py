### Get maximum depth of given binary tree using iterative BFS
###
from datastructure import *
import collections

def max_depth(root):
    if root is None:
        return 0

    queue = collections.deque([root])
    depth = 0

    while queue:
        depth += 1

        for _ in range(len(queue)):
            cur_root = queue.popleft()
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)
    return depth


input = TreeNode(val=3)
input.left = TreeNode(val=9)
input.right = TreeNode(val=20)
input.right.left = TreeNode(val=15)
input.right.right = TreeNode(val=7)

print(max_depth(input))