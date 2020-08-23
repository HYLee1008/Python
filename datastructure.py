class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.right = None
        self.left = None


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
