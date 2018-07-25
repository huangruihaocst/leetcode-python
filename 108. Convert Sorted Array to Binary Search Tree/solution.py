# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        n = len(nums)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(nums[0])
        i = n // 2
        root = TreeNode(nums[i])
        root.left = self.sortedArrayToBST(nums[:i])
        root.right = self.sortedArrayToBST(nums[i + 1:])
        return root


if __name__ == '__main__':
    s = Solution()
    t = s.sortedArrayToBST([-10, -3, 0, 5, 9])
    print(t.val)
    print(t.left.val)
    print(t.right.val)
    print(t.left.left.val)
    print(t.right.left.val)

