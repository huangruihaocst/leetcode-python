# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res = TreeNode(-1)
        curr = res

        def DFS(node):
            nonlocal curr
            if not node:
                return
            DFS(node.left)
            curr.right = TreeNode(node.val)
            curr = curr.right
            DFS(node.right)

        DFS(root)

        return res.right


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(5)
    t.r