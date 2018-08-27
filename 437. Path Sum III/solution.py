# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # Solution 1:
        if not root:
            return 0
        root.sum = [root.val]
        visit = [root]
        res = 1 if root.val == sum else 0
        while visit:
            new = list()
            for node in visit:
                for child in (node.left, node.right):
                    if child:
                        child.sum = [child.val] + [child.val + s for s in node.sum]
                        res += child.sum.count(sum)
                        new.append(child)
            visit = new
        return res

        # Solution 2:
        # TODO


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(10)
    t.left = TreeNode(5)
    t.right = TreeNode(-3)
    t.left.left = TreeNode(3)
    t.left.right = TreeNode(2)
    t.right.right = TreeNode(11)
    t.left.left.left = TreeNode(3)
    t.left.left.right = TreeNode(-2)
    t.left.right.right = TreeNode(1)
    print(s.pathSum(t, 8))
