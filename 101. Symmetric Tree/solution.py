# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def reverse(r):
            if not r:
                return None
            r.left, r.right = r.right, r.left
            reverse(r.left)
            reverse(r.right)

        def equals(r1, r2):
            if r1 is None and r2 is None:
                return True
            if (r1 is None and r2 is not None) or (r1 is not None and r2 is None):
                return False
            if r1.val != r2.val:
                return False
            return equals(r1.left, r2.left) and equals(r1.right, r2.right)

        if not root:
            return True
        right = root.right
        reverse(right)
        return equals(root.left, right)


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(2)
    print(s.isSymmetric(t))
