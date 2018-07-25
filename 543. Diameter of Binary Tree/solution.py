# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0

        def depth(node):
            if not node:
                return 0

            nonlocal res
            left = depth(node.left)
            right = depth(node.right)
            res = max(res, left + right)
            return 1 + max(left, right)

        depth(root)
        return res


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    t.left.left = TreeNode(4)
    t.left.right = TreeNode(5)
    print(s.diameterOfBinaryTree(t))
