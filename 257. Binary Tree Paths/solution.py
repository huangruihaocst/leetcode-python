# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return list()

        res = list()

        def DFS(node, past):
            past += '->' + str(node.val)
            if not node.left and not node.right:
                nonlocal res
                res.append(past)
            else:
                if node.left:
                    DFS(node.left, past)
                if node.right:
                    DFS(node.right, past)

        if root.left:
            DFS(root.left, str(root.val))
        if root.right:
            DFS(root.right, str(root.val))
        if not root.left and not root.right:
            return [str(root.val)]
        return res


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    t.left.right = TreeNode(5)
    print(s.binaryTreePaths(t))
