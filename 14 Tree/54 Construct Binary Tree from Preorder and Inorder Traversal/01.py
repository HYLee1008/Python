### Construct binary tree from preorder and inorder traversal
###
from datastructure import TreeNode


def build_tree(preorder, inorder):
    if inorder:
        index = inorder.index(preorder.pop(0))

        node = TreeNode(inorder[index])
        node.left = build_tree(preorder, inorder[0:index])
        node.right = build_tree(preorder, inorder[index + 1:])

        return node