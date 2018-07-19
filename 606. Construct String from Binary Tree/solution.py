# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """

        def DFS(node):
            if node is None:
                return ''
            if node.left is None and node.right is None:
                return str(node.val)
            if node.right is None:
                return str(node.val) + '(' +DFS(node.left) + ')'
            if node.left is None:
                return str(node.val) + '()(' + DFS(node.right) + ')'
            return str(node.val) + '(' + DFS(node.left) + ')(' + DFS(node.right) + ')'

        return DFS(t)


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    t.left.right = TreeNode(4)
    print(s.tree2str(t))
