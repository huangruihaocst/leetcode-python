# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return list()
        visit = [root]
        res = list()
        while visit:
            new = list()
            res.append([node.val for node in visit])
            for node in visit:
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            visit = new
        return res[::-1]


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(3)
    t.left = TreeNode(9)
    t.right = TreeNode(20)
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)
    print(s.levelOrderBottom(t))
