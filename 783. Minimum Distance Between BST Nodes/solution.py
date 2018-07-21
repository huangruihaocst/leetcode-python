# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDiffInBST(self, root):
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


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(4)
    t.left = TreeNode(2)
    t.right = TreeNode(6)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(3)
    print(s.minDiffInBST(t))
