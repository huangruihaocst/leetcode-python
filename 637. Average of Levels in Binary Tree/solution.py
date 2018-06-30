# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        level, res = list(), list()
        level.append(root)
        while level:
            res.append(sum(node.val for node in level) / len(level))
            new = list()
            for node in level:
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            level = new
        return res
                
if __name__ == '__main__':
    s = Solution()
    t = TreeNode(3)
    t.left = TreeNode(9)
    t.right = TreeNode(20)
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)
    print(s.averageOfLevels(t))
