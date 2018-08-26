# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        node = root
        p, q = p.val, q.val
        while True:
            if p < node.val < q or q < node.val < p:
                return node
            if p < node.val and q < node.val:
                node = node.left
            if p > node.val and q > node.val:
                node = node.right
            if node.val == p or node.val == q:
                return node


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(6)
    t.left = TreeNode(2)
    t.right = TreeNode(8)
    t.left.left = TreeNode(0)
    t.left.right = TreeNode(4)
    t.left.right.left = TreeNode(3)
    t.left.right.right = TreeNode(5)
    t.right.left = TreeNode(7)
    t.right.right = TreeNode(9)
    print(s.lowestCommonAncestor(t, TreeNode(2), TreeNode(8)).val)
