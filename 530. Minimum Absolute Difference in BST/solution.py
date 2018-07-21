# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        last, res = None, float('inf')

        def visit(node):
            nonlocal last, res
            if node.left:
                visit(node.left)
            if last is not None:
                diff = node.val - last
                if diff < res:
                    res = diff
            last = node.val
            if node.right:
                visit(node.right)

        visit(root)
        return res
