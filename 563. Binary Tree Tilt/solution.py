# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def add_sum(node):
            if not node.left and not node.right:  # leaf
                node.sum = node.val
            else:
                if node.left:
                    add_sum(node.left)
                if node.right:
                    add_sum(node.right)
                node.sum = node.val
                if node.left:
                    node.sum += node.left.sum
                if node.right:
                    node.sum += node.right.sum

        add_sum(root)

        res = 0

        def cal_tilt(node):
            if not node:
                return 0

            nonlocal res
            left = node.left.sum if node.left else 0
            right = node.right.sum if node.right else 0
            res += abs(left - right)
            cal_tilt(node.left)
            cal_tilt(node.right)

        cal_tilt(root)

        return res


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    print(s.findTilt(t))
