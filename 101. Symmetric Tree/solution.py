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
        # Solution 1:
        # def reverse(r):
        #     if not r:
        #         return None
        #     r.left, r.right = r.right, r.left
        #     reverse(r.left)
        #     reverse(r.right)
        #
        # def equals(r1, r2):
        #     if r1 is None and r2 is None:
        #         return True
        #     if (r1 is None and r2 is not None) or (r1 is not None and r2 is None):
        #         return False
        #     if r1.val != r2.val:
        #         return False
        #     return equals(r1.left, r2.left) and equals(r1.right, r2.right)
        #
        # if not root:
        #     return True
        # right = root.right
        # reverse(right)
        # return equals(root.left, right)

        # Solution 2:
        def symmetric(l, r):
            if l is None and r is None:
                return True
            if l is None or r is None:
                return False
            if l.val != r.val:
                return False
            return symmetric(l.left, r.right) and symmetric(l.right, r.left)

        if not root:
            return True
        return symmetric(root.left, root.right)


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(2)
    t.left.left = TreeNode(3)
    # t.left.right = TreeNode(4)
    # t.right.left = TreeNode(4)
    t.right.left = TreeNode(3)
    print(s.isSymmetric(t))
