# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        res = None
        _min = float('inf')

        def find(node):
            if not node:
                return
            nonlocal res, _min
            if abs(node.val - target) < _min:
                res = node.val
                _min = abs(node.val - target)
            if node.val > target:
                find(node.left)
            elif node.val < target:
                find(node.right)
            else:
                res = int(target)
                _min = 0
                return

        find(root)
        return res


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(4)
    t.left = TreeNode(2)
    t.right = TreeNode(5)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(3)
    print(s.closestValue(t, 2.1))
