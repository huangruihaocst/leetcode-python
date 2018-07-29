# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
#         self.right = None


class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """

        def DFS(node, v):
            if node.val == v:
                return node
            elif node.val > v:
                if node.left:
                    return DFS(node.left, v)
                else:
                    return None
            else:
                if node.right:
                    return DFS(node.right, v)

        return DFS(root, val)


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(4)
    t.left = TreeNode(2)
    t.right = TreeNode(7)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(3)
    res = s.searchBST(t, 2)
    print(res.val)
    print(res.left.val)
    print(res.right.val)

