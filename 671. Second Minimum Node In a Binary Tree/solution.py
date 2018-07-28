# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root.left and not root.right:
            return -1
        visit = [root]
        res = float('inf')
        while visit:
            r = float('inf')
            new = list()
            for node in visit:
                if r > node.val > root.val:
                    r = node.val
                if res == float('inf'):  # no answer now
                    if node.left:
                        new.append(node.left)
                        new.append(node.right)
                else:
                    if node.val == root.val and node.left:
                        new.append(node.left)
                        new.append(node.right)
            res = min(res, r)
            visit = new
        return res if res != float('inf') else -1


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(1)
    t.left = TreeNode(1)
    t.right = TreeNode(3)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(1)
    t.right.left = TreeNode(3)
    t.right.right = TreeNode(4)
    t.left.left.left = TreeNode(3)
    t.left.left.right = TreeNode(1)
    t.left.right.left = TreeNode(1)
    t.left.right.right = TreeNode(1)
    t.right.left.left = TreeNode(3)
    t.right.left.right = TreeNode(8)
    t.right.right.left = TreeNode(4)
    t.right.right.right = TreeNode(8)
    t.left.left.left.left = TreeNode(3)
    t.left.left.left.right = TreeNode(3)
    t.left.left.right.left = TreeNode(1)
    t.left.left.right.right = TreeNode(6)
    t.left.right.left.left = TreeNode(2)
    t.left.right.left.right = TreeNode(1)
    print(s.findSecondMinimumValue(t))
