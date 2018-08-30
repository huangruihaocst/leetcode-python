# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        res = True

        def height(node):
            nonlocal res
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            left = 1 + height(node.left)
            right = 1 + height(node.right)
            if abs(left - right) > 1:
                res = False
            return max(left, right)

        height(root)
        return res


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(1)
    t.right = TreeNode(2)
    t.right.right = TreeNode(3)
    print(s.isBalanced(t))
