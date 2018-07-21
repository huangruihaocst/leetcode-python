# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def DFS(node):
            if not node:
                return 0
            if node.left:
                if not node.left.left and not node.left.right:
                    return node.left.val + DFS(node.right)
                return DFS(node.left) + DFS(node.right)
            return DFS(node.right)

        return DFS(root)


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(3)
    t.left = TreeNode(9)
    t.right = TreeNode(20)
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)
    print(s.sumOfLeftLeaves(t))
